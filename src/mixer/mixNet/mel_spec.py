import torch
import torchaudio
import numpy as np


def mel_spec(acc, vox, rate):
    #win_length = n_fft
    #hop_length = win_length // 2
    transform = torchaudio.transforms.MelSpectrogram(sample_rate=rate, n_fft=2048)

    #mono
    if len(acc.shape) == 2:
        acc = np.mean(acc, axis=1)
    
    if len(vox.shape) == 2:
        vox = np.mean(vox, axis=1)


    acc = torch.from_numpy(acc).float()
    vox = torch.from_numpy(vox).float()

    acc_mel_spec = transform(acc)
    vox_mel_spec = transform(vox)

    acc = acc.detach().numpy()
    vox = vox.detach().numpy()


    def reshape(mel_spec):
        frameNum = mel_spec.shape[1]
        blockNum = int(frameNum / 64) #64*1024/44100 = 1.48s
        mel_spec = mel_spec.T[:-(frameNum - blockNum*64)].T
        mel_spec_matrix = torch.reshape(mel_spec, (128, blockNum, 64))
        mel_spec_matrix = mel_spec_matrix.permute(1, 2, 0) #blocks, time frame, freq frame
        return mel_spec_matrix

    try:
        acc_mel_spec = reshape(acc_mel_spec)
    except:
        print("reshape(acc_mel_spec)")
        return None
    
    try:
        vox_mel_spec = reshape(vox_mel_spec)
    except:
        print("reshape(vox_mel_spec)")
        return None

    dataset = torch.utils.data.TensorDataset(acc_mel_spec, vox_mel_spec)

    return dataset


