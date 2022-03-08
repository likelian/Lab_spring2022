{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 2,
			"revision" : 1,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 43.0, 100.0, 1348.0, 779.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-114",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 390.5, 363.5, 34.0, 23.0 ],
					"text" : "print"
				}

			}
, 			{
				"box" : 				{
					"bubble" : 1,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-27",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 108.5, 164.0, 137.0, 25.0 ],
					"text" : "open an audio file "
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-41",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 65.5, 165.0, 40.0, 23.0 ],
					"text" : "open"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-102",
					"linecount" : 3,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 102.5, 393.0, 260.0, 49.0 ],
					"text" : "open \"/Volumes/mix/Dataset/musdb18hq/train/ANiMAL - Easy Tiger/vocals.wav\""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-100",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 191.0, 314.5, 83.0, 22.0 ],
					"text" : "prepend open"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-99",
					"linecount" : 2,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 383.5, 292.0, 284.0, 35.0 ],
					"text" : "\"/Volumes/mix/Dataset/musdb18hq/train/ANiMAL - Easy Tiger/vocals.wav\""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-87",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 150.0, 237.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-66",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 464.0, 71.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-61",
					"maxclass" : "newobj",
					"numinlets" : 5,
					"numoutlets" : 4,
					"outlettype" : [ "int", "", "", "int" ],
					"patching_rect" : [ 383.5, 113.0, 61.0, 22.0 ],
					"text" : "counter"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-60",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 383.5, 71.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Helvetica",
					"fontsize" : 11.0,
					"id" : "obj-5",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 72.5, 21.0, 455.0, 19.0 ],
					"presentation_linecount" : 20,
					"text" : "read /Users/likelian/Desktop/Lab/Lab_spring2022/src/scripts/musdb18hq_train_vox_path.txt"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-37",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 383.5, 154.0, 53.0, 23.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-38",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 383.5, 193.0, 60.0, 23.0 ],
					"text" : "line $1"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "bang", "int" ],
					"patching_rect" : [ 383.5, 239.0, 40.0, 23.0 ],
					"text" : "text"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 412.5, 451.5, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "bang" ],
					"patching_rect" : [ 295.0, 509.0, 47.0, 22.0 ],
					"text" : "sfplay~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"local" : 1,
					"maxclass" : "ezdac~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 220.0, 658.5, 44.0, 44.0 ]
				}

			}
, 			{
				"box" : 				{
					"bubble" : 1,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-9",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 707.0, 416.0, 93.0, 25.0 ],
					"text" : "load a plug"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-47",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 397.666663999999969, 679.5, 146.0, 23.0 ],
					"text" : "print names @popup 1"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"format" : 6,
					"id" : "obj-63",
					"maxclass" : "flonum",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 670.5, 709.5, 54.0, 23.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-64",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 560.5, 709.5, 53.0, 23.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-65",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "int", "float" ],
					"patching_rect" : [ 560.5, 679.5, 129.0, 23.0 ],
					"text" : "unpack 0 0."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-70",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 555.5, 734.5, 105.0, 21.0 ],
					"text" : "parameter index"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-71",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 665.5, 734.5, 72.0, 21.0 ],
					"text" : "value (0-1)"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-74",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 560.5, 624.5, 378.0, 33.0 ],
					"presentation_linecount" : 2,
					"style" : "helpfile_label",
					"text" : "4th outlet: parameter change as a list when parameter is changed in the editing window or via a message in the inlet."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-43",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 640.0, 564.0, 59.0, 23.0 ],
					"text" : "get 1"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-48",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 640.0, 454.0, 59.0, 23.0 ],
					"text" : "params"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-55",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 640.0, 524.0, 30.0, 23.0 ],
					"text" : "4 1."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-56",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 640.0, 489.0, 59.0, 23.0 ],
					"text" : "Gain 0.5"
				}

			}
, 			{
				"box" : 				{
					"bubble" : 1,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-79",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 707.0, 486.0, 205.0, 25.0 ],
					"text" : "set value of named parameter"
				}

			}
, 			{
				"box" : 				{
					"bubble" : 1,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-80",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 707.0, 521.0, 225.0, 25.0 ],
					"text" : "set value of numbered parameter"
				}

			}
, 			{
				"box" : 				{
					"bubble" : 1,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-86",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 707.0, 451.5, 256.0, 25.0 ],
					"text" : "output parameter names to third outlet"
				}

			}
, 			{
				"box" : 				{
					"bubble" : 1,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-89",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 707.0, 553.5, 245.0, 40.0 ],
					"presentation_linecount" : 2,
					"text" : "output param value to fourth outlet - for more \"get\" syntax, see the ref "
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-12",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 640.0, 419.0, 59.0, 23.0 ],
					"text" : "plug"
				}

			}
, 			{
				"box" : 				{
					"autosave" : 1,
					"bgmode" : 0,
					"border" : 0,
					"clickthrough" : 0,
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-7",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 8,
					"offset" : [ 0.0, 0.0 ],
					"outlettype" : [ "signal", "signal", "", "list", "int", "", "", "" ],
					"patching_rect" : [ 343.0, 639.0, 194.0, 23.0 ],
					"save" : [ "#N", "vst~", "loaduniqueid", 0, ";" ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_invisible" : 1,
							"parameter_longname" : "vst~[3]",
							"parameter_shortname" : "vst~[3]",
							"parameter_type" : 3
						}

					}
,
					"saved_object_attributes" : 					{
						"parameter_enable" : 1,
						"parameter_mappable" : 0
					}
,
					"snapshot" : 					{
						"filetype" : "C74Snapshot",
						"version" : 2,
						"minorversion" : 0,
						"name" : "snapshotlist",
						"origin" : "vst~",
						"type" : "list",
						"subtype" : "Undefined",
						"embed" : 1,
						"snapshot" : 						{
							"pluginname" : "Accentize-Chameleon.vst3",
							"plugindisplayname" : "Chameleon",
							"pluginsavedname" : "/Library/Audio/Plug-Ins/VST3/Accentize-Chameleon.vst3",
							"pluginsaveduniqueid" : 0,
							"version" : 1,
							"isbank" : 0,
							"isbase64" : 1,
							"blob" : "14358.VMjLgz.N...OVMEUy.Ea0cVZtMEcgQWY9vSRC8Vav8lak4Fc9DCL2DiLtXUSpwzYLkkRt3hKOshYWElbAg1XqkjLh8FNrEFNHIESz4RZHYFUrEVZ3XTVuQSLYgCRRUEUYQ0RyfDdOkiKB8zPmYEVyUkQgsFNrElYtzlX0kkUZIWUVwDNHgGSwXVZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIiTv7VQjgGSUU0cDsFTwcVagEiYD0zZ2QUS10DUiA0YrYkSmcEVT0DahkmKUIFLznWVvbFLSITQDQUSUMkXB0zZiYENVAkcHASTBkzZjMyaGIVLHIiVm0jQSQycrgUaYIiXEMlQUgWSsEkQUUzXIMVLMQTTpQUTi01T4sFaMkVQUwjPmYkU0ACQUomd5kEd1QkVB8VaYgGSCEFcTk2XygidR8zYpkkcyn1TGETQQY2XxvTSYolU3gSLPwzXqQFMtACUPcmZRYTRWQVTMomR2QiZUQSSU0DLmYUSY0DLJ0zXvDlcDMjT0L1ZKc1X5U0LuUEUEUUaUA0YxnzbIQUUvT0PVEybnkETvXTSDUzZjACRSMEaUQzXPkkdLMTRvvjUuoGSoU0ZjEGR4MFZQQDUzcSLg0FL5M0ZzXkUYc1ZRIyaDIEdlcjX5QiZMM0X4I0S2oWTsUjLSoTPGE1ZIo2Xp0zZRc2ZCEFaQYEYTcVaR01cpEkLUo1X1QCaTQSRqQEdhAiX3gUaXMTU5kEVAcESsASLgMURGEUTQQUXEcVahAWTpEkTEQUSNclUQomXTkUaIsFVZQSLME0YDkEclIiXzH1QQQCUCQFZuoFRl4RahUWVVokbUwFS3fDdLEiYosDMqwFY1UUZUYGSxj0RA0lUvHlUVgGSrkEZmwFTL8FahI2aG4TM2Q0T3AidgoWTGEUdPczX3oldSMTRoIFUUUUS0jDQQcmbrEEdyoWXF8ldh4VQFM1UIQDYQUEajcmbwfEdlACTBslQhoURDIULPIyXucGaPUyaV0zcHUkTxETQY4VSSwzYMwVXHEzPjomavTUSMY0ToETQQQmaU0TQzDSVVE0PVU2ZDQVZUslXBsVdJIyXTIUdt.SVQkDUPo2Zw.ESyIkT4Y1UigzcFo0clk1R4MGUXkmaG0DL3PDUKQCUNETVoMlS2YjX1Y1TUkWVEQlPqMTSzblLPIzYvH1aqcETJcVQiQybBE1Rm0FY4UjLJYWVoA0UzXkXOMVQhk2YvPkLyQDUvfzThgTQ5M1RmQkTskjUgcWQUYkQMQkVwgzUYkzYoQELYYUX0QiPNsVQsIVbyHESYk0PTQiZosjTUs1XnUTLRgTVpQFLHMTSXQSLMoGVDM1ZygmXrMVUQ0zcTgkRiUDUGgSLZQmbrMFcMECUzgUUSgFMrIFUM01XEUDLMISVoQkZA0FT2omQiwTUrsjdEQzX48lQSISSxnkRIQzX5c1USs1XUYkTuQTSKM1QVcGUVQVLxQTUyUkLUQyZrwDLqECVBQiUUQSVFkULiMkUwg0QiYWUqwDdxYjVz3RdSEzYVgEcuczT3YmdYUWUGMELynFUzHFUZoWUoM1RAcTXqkjdioVSqI0cqMTXrEkUjQ0YsIUa2oVTxTkZiYGMrQEMIsFU3IFLhgGVsg0PUoWVXEzUL0FLwD1TIcTTQEEUgUzYsIFbQoVTRUDUM4zYVEkdhQUVskzZXoEMwzTTmQTVzYlLhQiXGEEMTMDYn8lZHYlKsIVcYYkVxUULLgCR3wTLlk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYWgEMEUEUvLmTSUWQUIlPzPUXRU0QUAELwPEdHUEYyfUURQWSwLVLIU0TL8VULgGVGQldTMkVwH1QYACLVIEMEYDYL8lZjwVR5Ika2YTUS0zThkGSwLUMMoVXtEUZjEWRTElT3nFYUcVQUQmXr0jRiYjTVMGaPoVVUMFVuoWS2gUQjMiaTEVUYQkVxXmQYkTUDEURAAiTQEzPL4zaW0DcEcjXwcSLMIUUrsDLTs1XWgCQNUSQFUEQqo1TS8Vag4VUS4DdmUUVH0TZhQzYpwjSzXTUrUTZPYzb5oDdqY0XNEUQREybFMFTEomVMUzTPQUSTM1QUUjU3MWLhEUQx.0RmoGSKclQhYGVrE0bEQ0TJ8VQTUSVSwTUYYkUuMmZU4VVoAkRUckVzUUUZ4VTDM1LlEyTtMmQLsVSx.USMAiRyEzQVQicwDlcyX0TPMmZQcUUpsjUQYkUVcmZjU0YwDEQUISSHMlZK4zcTU0T2QUSOcmQgUTUp0DdhESSn0jdicTR5MkPYcjXzLVLMomaUIVai0FVr8FUTMzaDIUbpcjVZcmURMzXTUkbqMzXVQiUNcVRWIVLDYTS2kzQQIWPSQ0Ryo1RzUkQh4FLpgjYtzlX0kkUZIWUF0DNHgGSvfTZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIST5UULJkWVwTUQvPzTm8ldUA0X5EVbzfmVwPSLXETVokUQmo1REEkUigUPv.0RmQkVycFLSMTVvzTV2QjVuETZZQ0XTUEZqMTSPQCZYMyaFokdqAiTZkDaRc2ZqQESvnGTvT0PhQWRxLEcpUzTvTUUTECLpY0QUolVvsFQZcUPxHUSQQTUBkkLMAWTFIFbEQUVVcVZZkWVrEFLTcjXYUULPsDLVI1SQISTwPDQVEmb50TaywVU2ciUiQzaqwTVucjUnMlURgTUDMUSUoVVL81ZRUCMVYUcygWUPcVLLoWUUMVRvXjSscGURgTVxfkdUc0TWcVdQMCTqsjdqUjTm8FUXICV5g0TmMkXCc1QMkWQqkEMuYjX3QCQNwTToszLHU0TAQiUMU0c5ElPqMTSzblLPIzYvH1aqcETHUTaUkmYwf0YMk2XvQiPRMzcV0zQqcjVvsVQNI0YEk0chQEVvfzZLo1YpMEbUICUZkULg4DLwnTTUQTUHU0ZPETPGokaq01XqACaSY0ZTAEcQcUUsUDULoELTwjbIMTSyk0UMMCV5IEVEoVV1EkUTESRpgjYtzlX0kkUZIWUV0DNHgGSvfTZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIST5UULJkWVwTUQvPzTm8ldUA0X5EVbzfmVwPSLXETVokUQmo1REEkUigUPv.0RmQkVycFLSMTVvzTV2QjVuETZZQ0XTUEZqMTSPQCZYMyaFokdqAiTZkDaRc2ZqQESvnGTvT0PhQWRxLEcpUzTvTUUTECLpY0QUolVvsFQZcUPxHUSQQTUBkkLMAWTFIFbEQUVVcVZZkWVrEFLTcjXYUULPsDLVI1SQISTwPDQVEmb50TaywVU2ciUiQzaqwTVucjUnMlURgTUDMUSUoVVL81ZRUCMVYUcygWUPcVLLoWUUMVRvXjSscGURgTVxfkdUc0TWcVdQMCTqsjdqUjTm8FUXICV5g0TmMkXCc1QMkWQqkEMuYjX3QCQNwTToszLHU0TAQiUMU0c5ElPqMTSzblLPIzYvH1aqcETHUTaUkmYwf0YMk2XvQiPRMzcV0zQqcjVvsVQNI0YEk0chQEVvfzZLo1YpMEbUICUZkULg4DLwnTTUQTUHU0ZPETPGokaq01XqACaSY0ZTAEcQcUUsUDULoELTwjbIMTSyk0UMMCV5IEVEoVV1EkUTESRpgjYtzlX0kkUZIWUr0DNHgGSwXVZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdl0FSyDzPMgGTxDkREQkXvj0UMgUUDwzbiQjTV8ldXgGVF4Tc3vFV2Q0PLkmbB0DMmICTBcFLh81ZWAkRmUzXzLmPgszYsQVdEIiR1kUZPcEMVI1SiUjX4cFLTIybDQELHMkXHUjdiszYTIUaIYUX2UTUVYTSToUbHcUVIcVZTASVVEVczHjSqUTahE2LRwTVYMDUznVZKIUUqMFZEEiTHkkZjACRC0DVzDSS5gEQis1b3IFaiUUTMcGUXozXEQ0Q3DiVzIGaiQWSwPEcXU0TnQCahQUSsMVQEASSxjUZToVPsA0c5YzXLUEaKoWQDMVduYzTxzjLZoTRDMldmc0TqMVUVI0aD0zRicjU2QkUjEibDU0bUISUzrFaLAyZwfkPzXUUzjkQYEyXSYUbXczX1U0ZLgmbFoEMtj2TAclUXQ2aGMEd1oWV0U0QSAyLpQEMhQkV5UUZisTPGE1ZIo2Xp0zZRc2ZCEFaQYEYTcVaR01cpEkLUo1X1QCaTQSRqQEdhAiX3gUaXMTU5kEVAcESsASLgMURGEUTQQUXEcVahAWTpEkTEQUSNclUQomXTkUaIsFVZQSLME0YDkEclIiXzH1QQQCUCQFZuoFRl4RahUWVVokbUESS3fDdLEiYosDMqwFY1UUZUYGSxj0RA0lUvHlUVgGSrkEZmwFTL8FahI2aG4TM2Q0T3AidgoWTGEUdPczX3oldSMTRoIFUUUUS0jDQQcmbrEEdyoWXF8ldh4VQFM1UIQDYQUEajcmbwfEdlACTBslQhoURDIULPIyXucGaPUyaV0zcHUkTxETQY4VSSwzYMwVXHEzPjomavTUSMY0ToETQQQmaU0TQzDSVVE0PVU2ZDQVZUslXBsVdJIyXTIUdt.SVQkDUPo2Zw.ESyIkT4Y1UjYDLDQERqsFSVQiQQEyYGIkZvPUUwPCUV0FM5wjbmkGTZcmZUoWSTE0ctzFVA0DaZYURDUkPqYESEkjLPYUVrsDUMMjStUDUSgWVFMkZmYjSLcFLiM2XGIkSYACUR0jQUISTSE1PEo1RJ0zZRAicwHFciISX3cmURIyaGMkLtbkXtc1UNQmawLlLXUUTAkTZgkVTEQkT2YjTpgiQiUSPEQURzHEYSUUdgIUV50TVAkGU2gDQZY2bBIlbmM0T3kjQiQCSCkEdioVVyPUaicTVqYUVvXkSRQSLXMWQUokLUQTXrE0ZiUSTqszLzDSXPslQgE2ZSkUPqQjVwfUQNIWRVwzQm0lVrQCZLomZSwDZAMUV0zTUPkmcwjEd3vlXxTDaj0TPSMlSmQUX3gEUP4TSEI1LUkFYz7VLPUybDwDQYYjXWMVaZoTSSE1Syo2THkkQL4DM5EEaI0lUsMGULk2XwD0TIoVVLcVQhs1c5IkT2YDSKMlQMkUUrIVcyoGVwHVLLA0ZoMUcEQTXvfjUNcTUEQUaQUkTDQCaRoDM5AUbLYUSXMmQQwVUoUUQYQjU2EzPVcVTVE1ZIQkX3QDahwVUpsjcUMUTAMmZHYlKsIVcYYkVxUkQNgCR3wDLHk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYxDkdUEiR4kULUUDLDM0YuoWUPMldgEGM3oULzDCVAkUZYUzYpsTQQY0XXEDLPszYTo0bmAyTCkELMk0cDo0aAklVTMFUUg1ZC0DTzfVVy7lQZo2ZvHkVIwlT2s1ZTwDL5AELUMjXzkjLSQmZEMELUUEUw.iZVcTUpoEbqQjVWEjLR0TTDUkPYISSvEkQhAWQTkkUmklV4kEagACUGIVVUECTKAiUh8TTxDULDQjUwImdM01brU0c2X0XD81ZLk0aGYEZiYkTHUEQS0TUpkESuslT0PiUVU2b3UETmECS5UUUikDLF4Ta2QkTHkkLXoWUWM0UmkWTy.0ZKo2ZEI0YuQEVxfkdXM0YSI1PmcTS4UzZYQyaFIFdzPjSLEUZKMCRUMUPzXUSUcmdgIzZC0DMmICTBcFLh81ZWAERE0VU4YVLXcVS4MFbzHjTCcmUMczZGoEbqUjSRcVQYcmXTgELHsFSpclZSAWUxPkVYESXNASLJEUUDUERUsFTAEzQZ41ZsM1Zvv1TVsFUPQWTWUUaEQESZACULIWRC0zbYcUSyfkdRgUQpkkcQYEUwjjZHYlKsIVcYYkVxUkUNgCR3wDLHk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYxDkdUEiR4kULUUDLDM0YuoWUPMldgEGM3oULzDCVAkUZYUzYpsTQQY0XXEDLPszYTo0bmAyTCkELMk0cDo0aAklVTMFUUg1ZC0DTzfVVy7lQZo2ZvHkVIwlT2s1ZTwDL5AELUMjXzkjLSQmZEMELUUEUw.iZVcTUpoEbqQjVWEjLR0TTDUkPYISSvEkQhAWQTkkUmklV4kEagACUGIVVUECTKAiUh8TTxDULDQjUwImdM01brU0c2X0XD81ZLk0aGYEZiYkTHUEQS0TUpkESuslT0PiUVU2b3UETmECS5UUUikDLF4Ta2QkTHkkLXoWUWM0UmkWTy.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.SVQkDUPo2Zw.ESyIkT4YlLQoWUwnTdYESUEACQSc1a5UETioWXwQCdZECMwfUPYkVVEclZKUTTVMFVAACTKcFUZM2YvL0PYASSYcGQZ8VPooEUiQUUns1PMAEMnk0LuYjV5sFLRoURrI0cqsFULAidPASUCIFcIIyTzoVQSASUUQULvnlUGUkZZA2ZDo0UAIiTMEEQUITVxzDbQYjXvUDUYY0YooUdYwVXvP0QhkUUw.0RvXkXOEkLQECQDYUbxoWSsMGaUc2MVMFQusFSY81QVg1XVIERUQzTMUkZYwzaqIUMzXkU0MGdUA0YwvjdUU0XIAiQN01cTIERYICV5U0USc0Y4E0LPs1R5sVQRc1aTgkLXoGVSc1ThMzYG0TdEsVVz7lQhgGMD4DSQk1RyfTUSEDMV0TU2oWXBs1PMQyYx.kPmAiXus1UPgTQsUUdlECVm0TdiAGMBI0P2YUSGs1QZA2ZE4jTmUTV2IFUXACRqwjZmo1TvUkLToUVwDlSvDiRQUEQUgTUqAUPAcjVtsVaisFLrMkUqQETzE0UU0VQTwjVvPESxkzPMMWVW0zLXomTXUjZYYWTVQULIoFRl4RahUWVVokbUYES4oWZHkGUowDcpckV0DzUMYUP4IVayQjXZUUdYkUR4gEaIYjVBcmZZg2crQ1LtczTMkzUSUWTGMFQMMzX5kzTR8TSpwDdQUUUv3VaPQTQ4okQIIiT0kkZRk2YVgkdisFTyTTUYUSQ4oUZIMjUCkDUZY2aqAERYMzXxrlQgIzasoELDkFUIcmQTo1YwvzcDECVzcFQLMSToY0UvnGVM0jQTQDMnYELToVXskUQMgENVI0LMYUU3kDUNEmXxDURMMDUsUzZPETTWo0P2omRI0zPjcTTWkUbL0VVWUEUSwTQrI0UAAST0MGaKEWVsEVZEoVSrUEQRQGUDkELmUDUCMGQR8FLFY0SMoVUxnVQS41ZFwDbQASTUkjUNomKqsDam0lVtE0UVszaqgkREckURcGUSMTUW0jczvlXOQiTVwTUWUUTYc0TZMFUQA2aVIkaiUjXKACQQQURpMlLtYTV18lUPsVVE4DbM0VVzU0TiY2ZUk0PyQUX2gCQicTVSAEVygmTxHVLZYUQ4EFLQolU3o1ZjgURwjURmQUTLACUQw1cpYkRu0VXYgSLJcUPEoUdPcUUvrFUgMiXFMURmo1XoE0Ui0zXE4zQmMTUzA0UVgTQrI0YikVTo0TQNcWSDQldLcEUrsVaZYWRsM0L1QTSzYVZT0TQpEFLTUzT0kDUNomZGQ1PIQjU4slUjEzYTIlUMMjVoUTLLIyarsDRMQTXvHFUj41aVY0LHUjUpUTdQcVUoQEdPYjTN8lUiM0aqkUczPUXwQTUQQ0YTUkPEQjXtclUjESUVElSYUkTAQiQiU0XVA0ctU0T2YGaLomdrMFLlkVTKcVUPwVPGkUTY0FTn4hPhgGNrk0a2YUV2A0TOgFSS0DdyHEYu81QhACVEwTdiEiT18VUM01ZqwTZYwFVtkDQSAWRGEVMmkFYLAiZh0DNFMldQoGS5EUaLkDN5AEdHcTUUUUZjITTTwTbYolXKgCaQoTSGo0YQISUBc1UTs1aWwTbMwFSX0jZP8VPsYkPmoVS5M1UZIWRpQFbUMESRsFQgAUTFoUdDMEVoQiQRYmYG0jViU0ToAidXAUTpsjVUMUTzMFaUomYvDVRmICVUkTaPQib3M1QqoGSPMlUTITQDM1aMQzTwoldLMSQwDFcMM0TskEUPA0XpIkRiUDUGgSLZQmbrMFcMYETwfkUQgDMREkZUcjUP0jdRgzZVEFV3nGTVM1TVwzYVokctYTUGU0ZXQCTCQEcXYDYvclQik0bpYEZuQkXYkTQS0TSTMFLtzVX3giZKk0cTMVUEs1XM8FLQUzaroURmESU1MGUSQTTqAULiklVpETaZETUrU0LtEiXrQiUMASPWY0ZMomTyUjLSo2Xp0TPmAiRKMVdYEWVUwTcUcTTZkzTVUyYqgUaqQjTEcGUSUTVFMkVuoFYzsFLgEmXEQkaMMzXUU0URM2Y4kESqQjTwzjQiACL5U0LhQjSTQiPik0YTgkREESSF0TLTMCQx.0LQkmXQkkUjAWPsIlSmMzT5MiPNIELTAEcUMUULgCaPQCTSQ1LMoFTX0zUZQSQDI0cYACSt0jUXkmXsoEcloGTxUUdQQyYroUVmkFUXEkULcTQV0jTIMTVHQiZZASSqYEa3v1TyMmTTUTTEIUUIQET1clQZQSVWk0bznVUIUjZgoWUvjUPEklUMUzPggGTSEVLUMjSFMGQVETVFIlZEs1XBkjPHYWRxDFaqYTXqUzTMgCR3wTLlk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYswzcMkVXQkTaMIzcDM1aqoVVwjTZQkzYV0DLHsVXFAiZLAWRxPUSmUTXV8VULgGVGQldTMkVwH1QYACLVIEMEYDYL8lZjwVR5Ika2YTUS0zThkGSwLUMMoVXtEUZjEWRTElT3nFYUcVQUQmXr0jRiYjTVMGaPoVVUMFVuoWS2gUQjMiaTEVUYQkVxXmQYkTUDEURAAiTQEzPL4zaW0DcEcjXwcSLMIUUrsDLTs1XWgCQNUSQFUEQqo1TS8Vag4VUS4DdmUUVH0TZhQzYpwjSzXTUrUTZPYzb5oDdqY0XNEUQREybFMFTEomVMUzTPQUSTM1QUUjU3MWLhEUQx.0RmoGSKclQhYGVrE0bEQ0TJ8VQTUSVSwTUYYkUuMmZU4VVoAkRUckVzUUUZ4VTDM1LlEyTtMmQLsVSx.USMAiRyEzQVQicwDlcyX0TPMmZQcUUpsjUQYkUVcmZjU0YwDEQUISSHMlZK4zcTU0T2QUSOcmQgUTUp0DdhESSn0jdicTR5MkPYcjXzLVLMomaUIVai0FVr8FUTMzaDIUbpcjVZcmURMzXTUkbqMzXVQiUNcVRWIVLDYTS2kzQQIWPSQ0Ryo1RzUkQh4FLpgjYtzlX0kkUZIWUVwTL5kFR4g0PNQmZWoUMAcUSVETdh01bDIlVUkWVYkTdXwVRFokP2olV3cGajMiaGMUSIc0T0E0QiQTSCMldIMkTO0jZLgWTUUELt0FTDUTdZYTRxHUcYolT4clUXo2XqA0LEUUV0TTdZkVRCY0PIQkV181ZPgTVCMlLqYTXB8VaZACQoQUR2YDUpcVLLcGQwfEcmQDSyDUZVcEL5gUSMYDUDQCZVACUpEVaYUTSXgiURMSSVUEdIQkSwIlLQkTSCQUaEsFTAE0UZMzc5oTRMMDYqcFUgQGLroEcmUDSv8lUX8zcV0zSYkmTDcVZVc1XVQ1QznGTIsVZSg2ZFY0cHk1XyD0TM8VV4MlZUcUXIs1UXMycpIUMYwFTKclQgQUSvvzcMkGVO8lLPQ2YF0TMywFTykDLSUSUEYEUzfWVw3ldYgTVvnkPQwVUvb1ZRICQoU0LmklTyU0ZQ81XCElZqQUTDsFQTsTQEwjcynFYvLiUhY2b3ElLHUUVzQ0TUEyXvL0LtcEVTEEUR4TSqQFcmYUSzfzQVs1Y5wDdQQjT3MiZgQUVVwjPYomTwgzUZACMDUERYIiV5ETUPEGLTwTPQACTvLFUUgURxnUdEUkXCMGQRkmbDokcAkVVFAiUP0zapYETu0VS2Q0ZYk0ZwHkUmwVSB8FUi8FMVU0amYTT5c1PZ8zYwnkcTEiXCAidTEmdFIFVqMTX0ETZg0TPvHkQiUUTzgUQYkUVEMUMUUjVGEEUiIiY5EEcyPzTU0TQSAyMDElbUQUTwfTdYICRw.kLioFTOkjZiY2ZxjkLPklU2MVLigVVrIUTMolTHMmTj41aEEVRMoWTUcmUNoWVqEFMDwlX2k0TXoGQsIFQ2YDSQMmdRQ2LVkkcmY0Tn4hPhgGNrk0a2YUV2I1TOgFSo0zLyHEYu81QhACVEwTdiEiT18VUM01ZqwTZYwFVtkDQSAWRGEVMmkFYLAiZh0DNFMldQoGS5EUaLkDN5AEdHcTUUUUZjITTTwTbYolXKgCaQoTSGo0YQISUBc1UTs1aWwTbMwFSX0jZP8VPsYkPmoVS5M1UZIWRpQFbUMESRsFQgAUTFoUdDMEVoQiQRYmYG0jViU0ToAidXAUTpsjVUMUTzMFaUomYvDVRmICVUkTaPQib3M1QqoGSPMlUTITQDM1aMQzTwoldLMSRo0zUiM0XNEkLgECTVwTdvnFSpk0TYUTR4wDTQkVVscVLLgUUxvDLEoGSY0jZj41XWUUPYEiVWcWLMgUTTM0LDYTSpEzPMIUUDQEUEQjSVUDLZsVVUgkbiMUX5oVUMkWUqQ0LpslTPMGZLoTV4MEaMYTXwLiUMI0bRUURQoGTscGahMyYvzjVzPUXD0zZSc0X5EURqYEUKM1ZPg0YpMELhUTXLUDaKMWTqUULtQDUzUjZjIUTDIEcUUTXynmZhgVTW4TdPwlX3olQMgTSrI0LyfmRwTUUT0TSrIlcTcEUR8VQjwTQxP0avPjX3AkUZQCTssDL3XDS0jUUNQiZpM0UAslU3MSLScGU4EUPqoFYKQCQUEmKEE0SYASTYUkUPEzc5wjLUsFT14VaSUTQW0jL2XzX2MVQVkFL5IkcHQDS3ImdgoTUCEVQAkWSpUzTRoTUwLkUIkmR2QCaTQWRDoURqM0XVUUajQ2crMESmIiRukkZhIGLpAkbAsFSyUUaTgVUxLVL2nmXyHldTkmKGQVcUs1XJUTaKgTREwjP2QDYvPDaYsFNFMFUQESVtsFaSoVRT0TdqckSDAiZYMiYW4zYMwVSzHGURETRBgjcIISXrslQgsVQC4DNHgGSvfTZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIST5UULJkWVwTUQvPzTm8ldUA0X5EVbzfmVwPSLXETVokUQmo1REEkUigUPv.0RmQkVycFLSMTVvzTV2QjVuETZZQ0XTUEZqMTSPQCZYMyaFokdqAiTZkDaRc2ZqQESvnGTvT0PhQWRxLEcpUzTvTUUTECLpY0QUolVvsFQZcUPxHUSQQTUBkkLMAWTFIFbEQUVVcVZZkWVrEFLTcjXYUULPsDLVI1SQISTwPDQVEmb50TaywVU2ciUiQzaqwTVucjUnMlURgTUDMUSUoVVL81ZRUCMVYUcygWUPcVLLoWUUMVRvXjSscGURgTVxfkdUc0TWcVdQMCTqsjdqUjTm8FUXICV5g0TmMkXCc1QMkWQqkEMuYjX3QCQNwTToszLHU0TAQiUMU0c5ElPqMTSzblLPIzYvH1aqcETHUTaUkmYwf0YMk2XvQiPRMzcV0zQqcjVvsVQNI0YEk0chQEVvfzZLo1YpMEbUICUZkULg4DLwnTTUQTUHU0ZPETPGokaq01XqACaSY0ZTAEcQcUUsUDULoELTwjbIMTSyk0UMMCV5IEVEoVV1EkUTESRpgjYtzlX0kkUZIWUVwDM5kFR4QUZLQmZWoUMAcUSVETdh01bDIlVUkWVYkTdXwVRFokP2olV3cGajMiaGMUSIc0T0E0QiQTSCMldIMkTO0jZLgWTUUELt0FTDUTdZYTRxHUcYolT4clUXo2XqA0LEUUV0TTdZkVRCY0PIQkV181ZPgTVCMlLqYTXB8VaZACQoQUR2YDUpcVLLcGQwfEcmQDSyDUZVcEL5gUSMYDUDQCZVACUpEVaYUTSXgiURMSSVUEdIQkSwIlLQkTSCQUaEsFTAE0UZMzc5oTRMMDYGE0UYEGSsk0UUQ0TLUDaRcUPvDUcyw1RwkUagkVQp0DaUQjTzQEQYAyYEQ0PyQjTuAiQV8TSpUkLpUzTtslQLAWTvDUUIYkS54xZKw1YsokaQckUK81ZXoTQWYkT2Q0TCU0UMYGMrI1SzHkULU0UUEUVWMkViQUTv8lUR41XEI1RvPTTTkjZiIiaFkkcuYETqkUQNAWSskEcUM0X1sVUYMzbTE1c3PzXGk0TPg0b3IkLhEiVVUTdgASTpYEdpsFYXkTLYkzYTEESvPUTrcmZVozasEVV3DiRWETQZkGTWUELqQUXyHlQSkzYpMVZQc0XMMVQNczYCUEcPckUHUDaRc1XoEUZMUjS20DQjoGSWQEaq0lV1kTaSMicD0DclkFUMUjZgACUEMUcIQkS5o1QjMTRDYUdqYEYAcFUhYUSCoUZEECSx7FaKgTSDEFLhQEYt8lUVMCREYkZEkWTmUUZTgGTFIkSuY0XS81ZYUGMTEVbDUUTTcFUUITQDIlamYEYwTkUg4TVUIUPzXzXUMlUPcmaUM0c1wFS5oGaiAiYoE0RmUETrEzQYEUVsAEZtHjX3gCaY81cVkEdtL0SnwzTMg2LRQ1aucjXvfUQLk2XwHkcuUUSss1ZLkVVrgkaIQzTvkzQgUyYoQFSvnlXMgiQioWT5wjdQ0FSIgidPgGRGUUUUkFYBEEULEWVpI1R3vVTJ0zQZcVTxTkPmcEUq81ULEWSrwDVMoFTuETaVIzYp0jdickVxkjZjAWUSwjTqQTXPEkQZkGQSgUZzXjT1Y1QMo0XUMUZvnGVPEkZKoUUSEEciwVU5YFLgkzYxfUUI0FTzHGdiczZ5wDTiYEUBUDQi8VSDMUbpoGSyLFQis1b3IFaiUUTMcGUXozXEQ0Q3DiVzIGaiQWSVAULXYUTHQiTQoVUGYETMomTHslUggEN5AkUiMkULclUZYmaFU0QUsFVz.0PTQGVFQFbmYzXYMmZVg1aTIVVIUzTM0DUiAiKsEFd3n1RYcGUiUUQqMVSuASTE8FaZkzYwTkcyQ0TDE0ZPEyXookZA0lVAUEaUMiawHFazXUSvDzUVsVS5I0bEIyT5MlZMEzYvnzRikWVwkUULUWUGEkVIMkU0b1ZX01ZDIUQ2Q0TEkkQSo0apQFcqASXwIVQT4VSCMVUUckTycVdYwzZDIULMYzXv.idUMiXD4DUzHzXYcFUXoTQwzjQMECUyPjLPMST4IVTYYEYvETah4zYCMkdyHjSRACUPQWUSUES3vFTz.0TjMSSpAEVMckVzTDQRcWVvvjaMYEV4IVaZQmY5AkbUkWTzbFaZk0YoQEVQYESGUjUMIURCkERznlVvzzZVwFNrM0byIEUEEUQRUURTAkcmYjVzj0UYMGMpUUREoVX5UELYETQoYUSEMTX3A0TgESUC4jQyQjUAkkQhoVQqMlPIIDRoUUahgWUrEld3.yX0kjLZ8FMwjUYYESXxEkUYgGLogTcTAiXqkjLhUmcVoUbUYTXuUDagUGTTkUdyYzX0EjLKwTQrgUcLQjVmAiUYIWUwDFc3TDU3gCaY81cVkUdIIDRqEkUZoGNrIVYvDSXpUkUOglKogjYLcjV0MlLLoFLogjcHIDRrgiQgoVUrI1TUYTXq0jQiUWRGI0ZqESVtE0UOgFQS0jcHIDRxUjQisFMwfEMvnWXpUkUOgFRCwjdlkFR4X2PTETRUAUSAIkVpASZHg1ZGI1YMIiXn4BZic1cVM1ZvjFR1MiPLg1Mn8zMtTETRUDUSYlZFkENHITXm81UjU1cwD1YQYkVzMFaHYFVWgkbUcUV3fjTLQmKogTcyLzSPUjZTEDLDgzaQY0SngzUYESUrIFZ3.SXzcmUjglKnM1Y2Y0XqASZHY2LBwDZ2f1S23RUPIUQTMkYpYTV3fDdhIGNFM1c2rFVm0jLhglKnM1Y2Y0XqASZHY2LBwDZ2f1S23RUPIUQTMkYpYTV3fDdhIGNFM1c2TTVq0jUXQSRBgTLEYTXvTkUOgFQCwjcyHDSncCZOciKUAkTEQ0TlolQYgCR3Ilb3XzX2cSQYg2ZxbkLUYzXn4BZic1cVM1ZvjFR24xPLQmKogTcyLzSPUjZTEDLDgzaQY0SnwzQgUWTWwTYmYkVscVLXASTsgjYXcEVxU0UYgCRnwjctLDS2MiPLg1Mn8zMtTETRUDUSYlZFkENHgmXxgiQic2MEEVciICVvDUaHYFVWgkbUcUV3fjPLQmKogTcyLzSPUjZTEDLDgzaQY0SnwzQgUWTWwTYvXEVwUkUiYGNvj0YqwVXn4BZic1cVM1ZvjFR1MiPNQiZS4DMpkVS2Y1TMkmKowjLLMTSncCZOciKUAkTEQ0TlolQYgCR3Ilb3XzX2cSQhgWUFk0Z2YEVzjjPHESQFEFLUY0Sn4RZKYGR3sTN1MDUAkTUP0TPRokZvjFR4cWLgoWQ4cUdQ0lXqEkLX4VRBgTLEYTXvTkUOglKosjcHg2R4X2PTETRUAUSAIkVpASZHk2cwDldEk2U5kzUYg1cVkEZtf1XmcmUisFLogjcyHDSncCZOciKUAkTEQ0TlolQYgCR3Ilb3XzX2cCLi8VTFMlaIIDRwTjQgASUV8DZtj1R1gDdKkic4szPmYEVyUkQgsFNrEVNt3hKt3hKt3hKt3hKtQUUCUEQTg2ZrM1YQcUVDUjQicVPP4RPHQEY1UTLhkWPP4RPL4hKi4hKt3hKt3hKtXlTU0DUQAURWoULEYzXqEEUXoWQFwyKIMzasA2atUlaz4COuX0TTMCTrU2Yo41TzEFck4C."
						}
,
						"snapshotlist" : 						{
							"current_snapshot" : 0,
							"entries" : [ 								{
									"filetype" : "C74Snapshot",
									"version" : 2,
									"minorversion" : 0,
									"name" : "Chameleon",
									"origin" : "Accentize-Chameleon.vst3",
									"type" : "VST3",
									"subtype" : "AudioEffect",
									"embed" : 0,
									"snapshot" : 									{
										"pluginname" : "Accentize-Chameleon.vst3",
										"plugindisplayname" : "Chameleon",
										"pluginsavedname" : "/Library/Audio/Plug-Ins/VST3/Accentize-Chameleon.vst3",
										"pluginsaveduniqueid" : 0,
										"version" : 1,
										"isbank" : 0,
										"isbase64" : 1,
										"blob" : "14358.VMjLgz.N...OVMEUy.Ea0cVZtMEcgQWY9vSRC8Vav8lak4Fc9DCL2DiLtXUSpwzYLkkRt3hKOshYWElbAg1XqkjLh8FNrEFNHIESz4RZHYFUrEVZ3XTVuQSLYgCRRUEUYQ0RyfDdOkiKB8zPmYEVyUkQgsFNrElYtzlX0kkUZIWUVwDNHgGSwXVZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIiTv7VQjgGSUU0cDsFTwcVagEiYD0zZ2QUS10DUiA0YrYkSmcEVT0DahkmKUIFLznWVvbFLSITQDQUSUMkXB0zZiYENVAkcHASTBkzZjMyaGIVLHIiVm0jQSQycrgUaYIiXEMlQUgWSsEkQUUzXIMVLMQTTpQUTi01T4sFaMkVQUwjPmYkU0ACQUomd5kEd1QkVB8VaYgGSCEFcTk2XygidR8zYpkkcyn1TGETQQY2XxvTSYolU3gSLPwzXqQFMtACUPcmZRYTRWQVTMomR2QiZUQSSU0DLmYUSY0DLJ0zXvDlcDMjT0L1ZKc1X5U0LuUEUEUUaUA0YxnzbIQUUvT0PVEybnkETvXTSDUzZjACRSMEaUQzXPkkdLMTRvvjUuoGSoU0ZjEGR4MFZQQDUzcSLg0FL5M0ZzXkUYc1ZRIyaDIEdlcjX5QiZMM0X4I0S2oWTsUjLSoTPGE1ZIo2Xp0zZRc2ZCEFaQYEYTcVaR01cpEkLUo1X1QCaTQSRqQEdhAiX3gUaXMTU5kEVAcESsASLgMURGEUTQQUXEcVahAWTpEkTEQUSNclUQomXTkUaIsFVZQSLME0YDkEclIiXzH1QQQCUCQFZuoFRl4RahUWVVokbUwFS3fDdLEiYosDMqwFY1UUZUYGSxj0RA0lUvHlUVgGSrkEZmwFTL8FahI2aG4TM2Q0T3AidgoWTGEUdPczX3oldSMTRoIFUUUUS0jDQQcmbrEEdyoWXF8ldh4VQFM1UIQDYQUEajcmbwfEdlACTBslQhoURDIULPIyXucGaPUyaV0zcHUkTxETQY4VSSwzYMwVXHEzPjomavTUSMY0ToETQQQmaU0TQzDSVVE0PVU2ZDQVZUslXBsVdJIyXTIUdt.SVQkDUPo2Zw.ESyIkT4Y1UigzcFo0clk1R4MGUXkmaG0DL3PDUKQCUNETVoMlS2YjX1Y1TUkWVEQlPqMTSzblLPIzYvH1aqcETJcVQiQybBE1Rm0FY4UjLJYWVoA0UzXkXOMVQhk2YvPkLyQDUvfzThgTQ5M1RmQkTskjUgcWQUYkQMQkVwgzUYkzYoQELYYUX0QiPNsVQsIVbyHESYk0PTQiZosjTUs1XnUTLRgTVpQFLHMTSXQSLMoGVDM1ZygmXrMVUQ0zcTgkRiUDUGgSLZQmbrMFcMECUzgUUSgFMrIFUM01XEUDLMISVoQkZA0FT2omQiwTUrsjdEQzX48lQSISSxnkRIQzX5c1USs1XUYkTuQTSKM1QVcGUVQVLxQTUyUkLUQyZrwDLqECVBQiUUQSVFkULiMkUwg0QiYWUqwDdxYjVz3RdSEzYVgEcuczT3YmdYUWUGMELynFUzHFUZoWUoM1RAcTXqkjdioVSqI0cqMTXrEkUjQ0YsIUa2oVTxTkZiYGMrQEMIsFU3IFLhgGVsg0PUoWVXEzUL0FLwD1TIcTTQEEUgUzYsIFbQoVTRUDUM4zYVEkdhQUVskzZXoEMwzTTmQTVzYlLhQiXGEEMTMDYn8lZHYlKsIVcYYkVxUULLgCR3wTLlk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYWgEMEUEUvLmTSUWQUIlPzPUXRU0QUAELwPEdHUEYyfUURQWSwLVLIU0TL8VULgGVGQldTMkVwH1QYACLVIEMEYDYL8lZjwVR5Ika2YTUS0zThkGSwLUMMoVXtEUZjEWRTElT3nFYUcVQUQmXr0jRiYjTVMGaPoVVUMFVuoWS2gUQjMiaTEVUYQkVxXmQYkTUDEURAAiTQEzPL4zaW0DcEcjXwcSLMIUUrsDLTs1XWgCQNUSQFUEQqo1TS8Vag4VUS4DdmUUVH0TZhQzYpwjSzXTUrUTZPYzb5oDdqY0XNEUQREybFMFTEomVMUzTPQUSTM1QUUjU3MWLhEUQx.0RmoGSKclQhYGVrE0bEQ0TJ8VQTUSVSwTUYYkUuMmZU4VVoAkRUckVzUUUZ4VTDM1LlEyTtMmQLsVSx.USMAiRyEzQVQicwDlcyX0TPMmZQcUUpsjUQYkUVcmZjU0YwDEQUISSHMlZK4zcTU0T2QUSOcmQgUTUp0DdhESSn0jdicTR5MkPYcjXzLVLMomaUIVai0FVr8FUTMzaDIUbpcjVZcmURMzXTUkbqMzXVQiUNcVRWIVLDYTS2kzQQIWPSQ0Ryo1RzUkQh4FLpgjYtzlX0kkUZIWUF0DNHgGSvfTZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIST5UULJkWVwTUQvPzTm8ldUA0X5EVbzfmVwPSLXETVokUQmo1REEkUigUPv.0RmQkVycFLSMTVvzTV2QjVuETZZQ0XTUEZqMTSPQCZYMyaFokdqAiTZkDaRc2ZqQESvnGTvT0PhQWRxLEcpUzTvTUUTECLpY0QUolVvsFQZcUPxHUSQQTUBkkLMAWTFIFbEQUVVcVZZkWVrEFLTcjXYUULPsDLVI1SQISTwPDQVEmb50TaywVU2ciUiQzaqwTVucjUnMlURgTUDMUSUoVVL81ZRUCMVYUcygWUPcVLLoWUUMVRvXjSscGURgTVxfkdUc0TWcVdQMCTqsjdqUjTm8FUXICV5g0TmMkXCc1QMkWQqkEMuYjX3QCQNwTToszLHU0TAQiUMU0c5ElPqMTSzblLPIzYvH1aqcETHUTaUkmYwf0YMk2XvQiPRMzcV0zQqcjVvsVQNI0YEk0chQEVvfzZLo1YpMEbUICUZkULg4DLwnTTUQTUHU0ZPETPGokaq01XqACaSY0ZTAEcQcUUsUDULoELTwjbIMTSyk0UMMCV5IEVEoVV1EkUTESRpgjYtzlX0kkUZIWUV0DNHgGSvfTZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIST5UULJkWVwTUQvPzTm8ldUA0X5EVbzfmVwPSLXETVokUQmo1REEkUigUPv.0RmQkVycFLSMTVvzTV2QjVuETZZQ0XTUEZqMTSPQCZYMyaFokdqAiTZkDaRc2ZqQESvnGTvT0PhQWRxLEcpUzTvTUUTECLpY0QUolVvsFQZcUPxHUSQQTUBkkLMAWTFIFbEQUVVcVZZkWVrEFLTcjXYUULPsDLVI1SQISTwPDQVEmb50TaywVU2ciUiQzaqwTVucjUnMlURgTUDMUSUoVVL81ZRUCMVYUcygWUPcVLLoWUUMVRvXjSscGURgTVxfkdUc0TWcVdQMCTqsjdqUjTm8FUXICV5g0TmMkXCc1QMkWQqkEMuYjX3QCQNwTToszLHU0TAQiUMU0c5ElPqMTSzblLPIzYvH1aqcETHUTaUkmYwf0YMk2XvQiPRMzcV0zQqcjVvsVQNI0YEk0chQEVvfzZLo1YpMEbUICUZkULg4DLwnTTUQTUHU0ZPETPGokaq01XqACaSY0ZTAEcQcUUsUDULoELTwjbIMTSyk0UMMCV5IEVEoVV1EkUTESRpgjYtzlX0kkUZIWUr0DNHgGSwXVZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdl0FSyDzPMgGTxDkREQkXvj0UMgUUDwzbiQjTV8ldXgGVF4Tc3vFV2Q0PLkmbB0DMmICTBcFLh81ZWAkRmUzXzLmPgszYsQVdEIiR1kUZPcEMVI1SiUjX4cFLTIybDQELHMkXHUjdiszYTIUaIYUX2UTUVYTSToUbHcUVIcVZTASVVEVczHjSqUTahE2LRwTVYMDUznVZKIUUqMFZEEiTHkkZjACRC0DVzDSS5gEQis1b3IFaiUUTMcGUXozXEQ0Q3DiVzIGaiQWSwPEcXU0TnQCahQUSsMVQEASSxjUZToVPsA0c5YzXLUEaKoWQDMVduYzTxzjLZoTRDMldmc0TqMVUVI0aD0zRicjU2QkUjEibDU0bUISUzrFaLAyZwfkPzXUUzjkQYEyXSYUbXczX1U0ZLgmbFoEMtj2TAclUXQ2aGMEd1oWV0U0QSAyLpQEMhQkV5UUZisTPGE1ZIo2Xp0zZRc2ZCEFaQYEYTcVaR01cpEkLUo1X1QCaTQSRqQEdhAiX3gUaXMTU5kEVAcESsASLgMURGEUTQQUXEcVahAWTpEkTEQUSNclUQomXTkUaIsFVZQSLME0YDkEclIiXzH1QQQCUCQFZuoFRl4RahUWVVokbUESS3fDdLEiYosDMqwFY1UUZUYGSxj0RA0lUvHlUVgGSrkEZmwFTL8FahI2aG4TM2Q0T3AidgoWTGEUdPczX3oldSMTRoIFUUUUS0jDQQcmbrEEdyoWXF8ldh4VQFM1UIQDYQUEajcmbwfEdlACTBslQhoURDIULPIyXucGaPUyaV0zcHUkTxETQY4VSSwzYMwVXHEzPjomavTUSMY0ToETQQQmaU0TQzDSVVE0PVU2ZDQVZUslXBsVdJIyXTIUdt.SVQkDUPo2Zw.ESyIkT4Y1UjYDLDQERqsFSVQiQQEyYGIkZvPUUwPCUV0FM5wjbmkGTZcmZUoWSTE0ctzFVA0DaZYURDUkPqYESEkjLPYUVrsDUMMjStUDUSgWVFMkZmYjSLcFLiM2XGIkSYACUR0jQUISTSE1PEo1RJ0zZRAicwHFciISX3cmURIyaGMkLtbkXtc1UNQmawLlLXUUTAkTZgkVTEQkT2YjTpgiQiUSPEQURzHEYSUUdgIUV50TVAkGU2gDQZY2bBIlbmM0T3kjQiQCSCkEdioVVyPUaicTVqYUVvXkSRQSLXMWQUokLUQTXrE0ZiUSTqszLzDSXPslQgE2ZSkUPqQjVwfUQNIWRVwzQm0lVrQCZLomZSwDZAMUV0zTUPkmcwjEd3vlXxTDaj0TPSMlSmQUX3gEUP4TSEI1LUkFYz7VLPUybDwDQYYjXWMVaZoTSSE1Syo2THkkQL4DM5EEaI0lUsMGULk2XwD0TIoVVLcVQhs1c5IkT2YDSKMlQMkUUrIVcyoGVwHVLLA0ZoMUcEQTXvfjUNcTUEQUaQUkTDQCaRoDM5AUbLYUSXMmQQwVUoUUQYQjU2EzPVcVTVE1ZIQkX3QDahwVUpsjcUMUTAMmZHYlKsIVcYYkVxUkQNgCR3wDLHk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYxDkdUEiR4kULUUDLDM0YuoWUPMldgEGM3oULzDCVAkUZYUzYpsTQQY0XXEDLPszYTo0bmAyTCkELMk0cDo0aAklVTMFUUg1ZC0DTzfVVy7lQZo2ZvHkVIwlT2s1ZTwDL5AELUMjXzkjLSQmZEMELUUEUw.iZVcTUpoEbqQjVWEjLR0TTDUkPYISSvEkQhAWQTkkUmklV4kEagACUGIVVUECTKAiUh8TTxDULDQjUwImdM01brU0c2X0XD81ZLk0aGYEZiYkTHUEQS0TUpkESuslT0PiUVU2b3UETmECS5UUUikDLF4Ta2QkTHkkLXoWUWM0UmkWTy.0ZKo2ZEI0YuQEVxfkdXM0YSI1PmcTS4UzZYQyaFIFdzPjSLEUZKMCRUMUPzXUSUcmdgIzZC0DMmICTBcFLh81ZWAERE0VU4YVLXcVS4MFbzHjTCcmUMczZGoEbqUjSRcVQYcmXTgELHsFSpclZSAWUxPkVYESXNASLJEUUDUERUsFTAEzQZ41ZsM1Zvv1TVsFUPQWTWUUaEQESZACULIWRC0zbYcUSyfkdRgUQpkkcQYEUwjjZHYlKsIVcYYkVxUkUNgCR3wDLHk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYxDkdUEiR4kULUUDLDM0YuoWUPMldgEGM3oULzDCVAkUZYUzYpsTQQY0XXEDLPszYTo0bmAyTCkELMk0cDo0aAklVTMFUUg1ZC0DTzfVVy7lQZo2ZvHkVIwlT2s1ZTwDL5AELUMjXzkjLSQmZEMELUUEUw.iZVcTUpoEbqQjVWEjLR0TTDUkPYISSvEkQhAWQTkkUmklV4kEagACUGIVVUECTKAiUh8TTxDULDQjUwImdM01brU0c2X0XD81ZLk0aGYEZiYkTHUEQS0TUpkESuslT0PiUVU2b3UETmECS5UUUikDLF4Ta2QkTHkkLXoWUWM0UmkWTy.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.SVQkDUPo2Zw.ESyIkT4YlLQoWUwnTdYESUEACQSc1a5UETioWXwQCdZECMwfUPYkVVEclZKUTTVMFVAACTKcFUZM2YvL0PYASSYcGQZ8VPooEUiQUUns1PMAEMnk0LuYjV5sFLRoURrI0cqsFULAidPASUCIFcIIyTzoVQSASUUQULvnlUGUkZZA2ZDo0UAIiTMEEQUITVxzDbQYjXvUDUYY0YooUdYwVXvP0QhkUUw.0RvXkXOEkLQECQDYUbxoWSsMGaUc2MVMFQusFSY81QVg1XVIERUQzTMUkZYwzaqIUMzXkU0MGdUA0YwvjdUU0XIAiQN01cTIERYICV5U0USc0Y4E0LPs1R5sVQRc1aTgkLXoGVSc1ThMzYG0TdEsVVz7lQhgGMD4DSQk1RyfTUSEDMV0TU2oWXBs1PMQyYx.kPmAiXus1UPgTQsUUdlECVm0TdiAGMBI0P2YUSGs1QZA2ZE4jTmUTV2IFUXACRqwjZmo1TvUkLToUVwDlSvDiRQUEQUgTUqAUPAcjVtsVaisFLrMkUqQETzE0UU0VQTwjVvPESxkzPMMWVW0zLXomTXUjZYYWTVQULIoFRl4RahUWVVokbUYES4oWZHkGUowDcpckV0DzUMYUP4IVayQjXZUUdYkUR4gEaIYjVBcmZZg2crQ1LtczTMkzUSUWTGMFQMMzX5kzTR8TSpwDdQUUUv3VaPQTQ4okQIIiT0kkZRk2YVgkdisFTyTTUYUSQ4oUZIMjUCkDUZY2aqAERYMzXxrlQgIzasoELDkFUIcmQTo1YwvzcDECVzcFQLMSToY0UvnGVM0jQTQDMnYELToVXskUQMgENVI0LMYUU3kDUNEmXxDURMMDUsUzZPETTWo0P2omRI0zPjcTTWkUbL0VVWUEUSwTQrI0UAAST0MGaKEWVsEVZEoVSrUEQRQGUDkELmUDUCMGQR8FLFY0SMoVUxnVQS41ZFwDbQASTUkjUNomKqsDam0lVtE0UVszaqgkREckURcGUSMTUW0jczvlXOQiTVwTUWUUTYc0TZMFUQA2aVIkaiUjXKACQQQURpMlLtYTV18lUPsVVE4DbM0VVzU0TiY2ZUk0PyQUX2gCQicTVSAEVygmTxHVLZYUQ4EFLQolU3o1ZjgURwjURmQUTLACUQw1cpYkRu0VXYgSLJcUPEoUdPcUUvrFUgMiXFMURmo1XoE0Ui0zXE4zQmMTUzA0UVgTQrI0YikVTo0TQNcWSDQldLcEUrsVaZYWRsM0L1QTSzYVZT0TQpEFLTUzT0kDUNomZGQ1PIQjU4slUjEzYTIlUMMjVoUTLLIyarsDRMQTXvHFUj41aVY0LHUjUpUTdQcVUoQEdPYjTN8lUiM0aqkUczPUXwQTUQQ0YTUkPEQjXtclUjESUVElSYUkTAQiQiU0XVA0ctU0T2YGaLomdrMFLlkVTKcVUPwVPGkUTY0FTn4hPhgGNrk0a2YUV2A0TOgFSS0DdyHEYu81QhACVEwTdiEiT18VUM01ZqwTZYwFVtkDQSAWRGEVMmkFYLAiZh0DNFMldQoGS5EUaLkDN5AEdHcTUUUUZjITTTwTbYolXKgCaQoTSGo0YQISUBc1UTs1aWwTbMwFSX0jZP8VPsYkPmoVS5M1UZIWRpQFbUMESRsFQgAUTFoUdDMEVoQiQRYmYG0jViU0ToAidXAUTpsjVUMUTzMFaUomYvDVRmICVUkTaPQib3M1QqoGSPMlUTITQDM1aMQzTwoldLMSQwDFcMM0TskEUPA0XpIkRiUDUGgSLZQmbrMFcMYETwfkUQgDMREkZUcjUP0jdRgzZVEFV3nGTVM1TVwzYVokctYTUGU0ZXQCTCQEcXYDYvclQik0bpYEZuQkXYkTQS0TSTMFLtzVX3giZKk0cTMVUEs1XM8FLQUzaroURmESU1MGUSQTTqAULiklVpETaZETUrU0LtEiXrQiUMASPWY0ZMomTyUjLSo2Xp0TPmAiRKMVdYEWVUwTcUcTTZkzTVUyYqgUaqQjTEcGUSUTVFMkVuoFYzsFLgEmXEQkaMMzXUU0URM2Y4kESqQjTwzjQiACL5U0LhQjSTQiPik0YTgkREESSF0TLTMCQx.0LQkmXQkkUjAWPsIlSmMzT5MiPNIELTAEcUMUULgCaPQCTSQ1LMoFTX0zUZQSQDI0cYACSt0jUXkmXsoEcloGTxUUdQQyYroUVmkFUXEkULcTQV0jTIMTVHQiZZASSqYEa3v1TyMmTTUTTEIUUIQET1clQZQSVWk0bznVUIUjZgoWUvjUPEklUMUzPggGTSEVLUMjSFMGQVETVFIlZEs1XBkjPHYWRxDFaqYTXqUzTMgCR3wTLlk1RzrFajYWUoUkcLISVKETaVAiXVYEdLwVVncFaPwzarIlbucjS0bGUSgGL5EldQcTT4A0QigmZ5M0PIklXTUUUMUSRDE0cxwVT3MmdgYza5IlaEYzXWkDQjEUUrQ1cxECV3YFLPIzZFIlVIQjTw.kLi81crAUMuYUS2gTURIWPEkkaMMESm0DaggTPCQldtASUM0jUSkVPEEEctUUSEQSLYYUTCYUcqQDYoU0ZhIzZ4ojLiQkT44BLYEURTAkdqECTLMmTRkmYswzcMkVXQkTaMIzcDM1aqoVVwjTZQkzYV0DLHsVXFAiZLAWRxPUSmUTXV8VULgGVGQldTMkVwH1QYACLVIEMEYDYL8lZjwVR5Ika2YTUS0zThkGSwLUMMoVXtEUZjEWRTElT3nFYUcVQUQmXr0jRiYjTVMGaPoVVUMFVuoWS2gUQjMiaTEVUYQkVxXmQYkTUDEURAAiTQEzPL4zaW0DcEcjXwcSLMIUUrsDLTs1XWgCQNUSQFUEQqo1TS8Vag4VUS4DdmUUVH0TZhQzYpwjSzXTUrUTZPYzb5oDdqY0XNEUQREybFMFTEomVMUzTPQUSTM1QUUjU3MWLhEUQx.0RmoGSKclQhYGVrE0bEQ0TJ8VQTUSVSwTUYYkUuMmZU4VVoAkRUckVzUUUZ4VTDM1LlEyTtMmQLsVSx.USMAiRyEzQVQicwDlcyX0TPMmZQcUUpsjUQYkUVcmZjU0YwDEQUISSHMlZK4zcTU0T2QUSOcmQgUTUp0DdhESSn0jdicTR5MkPYcjXzLVLMomaUIVai0FVr8FUTMzaDIUbpcjVZcmURMzXTUkbqMzXVQiUNcVRWIVLDYTS2kzQQIWPSQ0Ryo1RzUkQh4FLpgjYtzlX0kkUZIWUVwTL5kFR4g0PNQmZWoUMAcUSVETdh01bDIlVUkWVYkTdXwVRFokP2olV3cGajMiaGMUSIc0T0E0QiQTSCMldIMkTO0jZLgWTUUELt0FTDUTdZYTRxHUcYolT4clUXo2XqA0LEUUV0TTdZkVRCY0PIQkV181ZPgTVCMlLqYTXB8VaZACQoQUR2YDUpcVLLcGQwfEcmQDSyDUZVcEL5gUSMYDUDQCZVACUpEVaYUTSXgiURMSSVUEdIQkSwIlLQkTSCQUaEsFTAE0UZMzc5oTRMMDYqcFUgQGLroEcmUDSv8lUX8zcV0zSYkmTDcVZVc1XVQ1QznGTIsVZSg2ZFY0cHk1XyD0TM8VV4MlZUcUXIs1UXMycpIUMYwFTKclQgQUSvvzcMkGVO8lLPQ2YF0TMywFTykDLSUSUEYEUzfWVw3ldYgTVvnkPQwVUvb1ZRICQoU0LmklTyU0ZQ81XCElZqQUTDsFQTsTQEwjcynFYvLiUhY2b3ElLHUUVzQ0TUEyXvL0LtcEVTEEUR4TSqQFcmYUSzfzQVs1Y5wDdQQjT3MiZgQUVVwjPYomTwgzUZACMDUERYIiV5ETUPEGLTwTPQACTvLFUUgURxnUdEUkXCMGQRkmbDokcAkVVFAiUP0zapYETu0VS2Q0ZYk0ZwHkUmwVSB8FUi8FMVU0amYTT5c1PZ8zYwnkcTEiXCAidTEmdFIFVqMTX0ETZg0TPvHkQiUUTzgUQYkUVEMUMUUjVGEEUiIiY5EEcyPzTU0TQSAyMDElbUQUTwfTdYICRw.kLioFTOkjZiY2ZxjkLPklU2MVLigVVrIUTMolTHMmTj41aEEVRMoWTUcmUNoWVqEFMDwlX2k0TXoGQsIFQ2YDSQMmdRQ2LVkkcmY0Tn4hPhgGNrk0a2YUV2I1TOgFSo0zLyHEYu81QhACVEwTdiEiT18VUM01ZqwTZYwFVtkDQSAWRGEVMmkFYLAiZh0DNFMldQoGS5EUaLkDN5AEdHcTUUUUZjITTTwTbYolXKgCaQoTSGo0YQISUBc1UTs1aWwTbMwFSX0jZP8VPsYkPmoVS5M1UZIWRpQFbUMESRsFQgAUTFoUdDMEVoQiQRYmYG0jViU0ToAidXAUTpsjVUMUTzMFaUomYvDVRmICVUkTaPQib3M1QqoGSPMlUTITQDM1aMQzTwoldLMSRo0zUiM0XNEkLgECTVwTdvnFSpk0TYUTR4wDTQkVVscVLLgUUxvDLEoGSY0jZj41XWUUPYEiVWcWLMgUTTM0LDYTSpEzPMIUUDQEUEQjSVUDLZsVVUgkbiMUX5oVUMkWUqQ0LpslTPMGZLoTV4MEaMYTXwLiUMI0bRUURQoGTscGahMyYvzjVzPUXD0zZSc0X5EURqYEUKM1ZPg0YpMELhUTXLUDaKMWTqUULtQDUzUjZjIUTDIEcUUTXynmZhgVTW4TdPwlX3olQMgTSrI0LyfmRwTUUT0TSrIlcTcEUR8VQjwTQxP0avPjX3AkUZQCTssDL3XDS0jUUNQiZpM0UAslU3MSLScGU4EUPqoFYKQCQUEmKEE0SYASTYUkUPEzc5wjLUsFT14VaSUTQW0jL2XzX2MVQVkFL5IkcHQDS3ImdgoTUCEVQAkWSpUzTRoTUwLkUIkmR2QCaTQWRDoURqM0XVUUajQ2crMESmIiRukkZhIGLpAkbAsFSyUUaTgVUxLVL2nmXyHldTkmKGQVcUs1XJUTaKgTREwjP2QDYvPDaYsFNFMFUQESVtsFaSoVRT0TdqckSDAiZYMiYW4zYMwVSzHGURETRBgjcIISXrslQgsVQC4DNHgGSvfTZKQyZrQlcUkVU1wjLYsTPsYELhYkU3wDaYg1YrAESuwlXx81QNUycTMEdvnWX5E0QQkGTGMFdpo2TCkTZhQUUU0TMIQTT2IGaQg2b5ElQuomXtUjQicURDQVTUwFY2IWLXgmYv.kPqYjXZkDQRECTxL1a2wFT07lUMcGRUIkbAUTVt0zTLcVSrEFRAMDY54FLU0TSVMUZAUTTz4VUMUDMwjkUQMjU0sFQjkVUqIlPqkmRxLFURkmKvjUTIQET5sVLPwzbRIUdlIST5UULJkWVwTUQvPzTm8ldUA0X5EVbzfmVwPSLXETVokUQmo1REEkUigUPv.0RmQkVycFLSMTVvzTV2QjVuETZZQ0XTUEZqMTSPQCZYMyaFokdqAiTZkDaRc2ZqQESvnGTvT0PhQWRxLEcpUzTvTUUTECLpY0QUolVvsFQZcUPxHUSQQTUBkkLMAWTFIFbEQUVVcVZZkWVrEFLTcjXYUULPsDLVI1SQISTwPDQVEmb50TaywVU2ciUiQzaqwTVucjUnMlURgTUDMUSUoVVL81ZRUCMVYUcygWUPcVLLoWUUMVRvXjSscGURgTVxfkdUc0TWcVdQMCTqsjdqUjTm8FUXICV5g0TmMkXCc1QMkWQqkEMuYjX3QCQNwTToszLHU0TAQiUMU0c5ElPqMTSzblLPIzYvH1aqcETHUTaUkmYwf0YMk2XvQiPRMzcV0zQqcjVvsVQNI0YEk0chQEVvfzZLo1YpMEbUICUZkULg4DLwnTTUQTUHU0ZPETPGokaq01XqACaSY0ZTAEcQcUUsUDULoELTwjbIMTSyk0UMMCV5IEVEoVV1EkUTESRpgjYtzlX0kkUZIWUVwDM5kFR4QUZLQmZWoUMAcUSVETdh01bDIlVUkWVYkTdXwVRFokP2olV3cGajMiaGMUSIc0T0E0QiQTSCMldIMkTO0jZLgWTUUELt0FTDUTdZYTRxHUcYolT4clUXo2XqA0LEUUV0TTdZkVRCY0PIQkV181ZPgTVCMlLqYTXB8VaZACQoQUR2YDUpcVLLcGQwfEcmQDSyDUZVcEL5gUSMYDUDQCZVACUpEVaYUTSXgiURMSSVUEdIQkSwIlLQkTSCQUaEsFTAE0UZMzc5oTRMMDYGE0UYEGSsk0UUQ0TLUDaRcUPvDUcyw1RwkUagkVQp0DaUQjTzQEQYAyYEQ0PyQjTuAiQV8TSpUkLpUzTtslQLAWTvDUUIYkS54xZKw1YsokaQckUK81ZXoTQWYkT2Q0TCU0UMYGMrI1SzHkULU0UUEUVWMkViQUTv8lUR41XEI1RvPTTTkjZiIiaFkkcuYETqkUQNAWSskEcUM0X1sVUYMzbTE1c3PzXGk0TPg0b3IkLhEiVVUTdgASTpYEdpsFYXkTLYkzYTEESvPUTrcmZVozasEVV3DiRWETQZkGTWUELqQUXyHlQSkzYpMVZQc0XMMVQNczYCUEcPckUHUDaRc1XoEUZMUjS20DQjoGSWQEaq0lV1kTaSMicD0DclkFUMUjZgACUEMUcIQkS5o1QjMTRDYUdqYEYAcFUhYUSCoUZEECSx7FaKgTSDEFLhQEYt8lUVMCREYkZEkWTmUUZTgGTFIkSuY0XS81ZYUGMTEVbDUUTTcFUUITQDIlamYEYwTkUg4TVUIUPzXzXUMlUPcmaUM0c1wFS5oGaiAiYoE0RmUETrEzQYEUVsAEZtHjX3gCaY81cVkEdtL0SnwzTMg2LRQ1aucjXvfUQLk2XwHkcuUUSss1ZLkVVrgkaIQzTvkzQgUyYoQFSvnlXMgiQioWT5wjdQ0FSIgidPgGRGUUUUkFYBEEULEWVpI1R3vVTJ0zQZcVTxTkPmcEUq81ULEWSrwDVMoFTuETaVIzYp0jdickVxkjZjAWUSwjTqQTXPEkQZkGQSgUZzXjT1Y1QMo0XUMUZvnGVPEkZKoUUSEEciwVU5YFLgkzYxfUUI0FTzHGdiczZ5wDTiYEUBUDQi8VSDMUbpoGSyLFQis1b3IFaiUUTMcGUXozXEQ0Q3DiVzIGaiQWSVAULXYUTHQiTQoVUGYETMomTHslUggEN5AkUiMkULclUZYmaFU0QUsFVz.0PTQGVFQFbmYzXYMmZVg1aTIVVIUzTM0DUiAiKsEFd3n1RYcGUiUUQqMVSuASTE8FaZkzYwTkcyQ0TDE0ZPEyXookZA0lVAUEaUMiawHFazXUSvDzUVsVS5I0bEIyT5MlZMEzYvnzRikWVwkUULUWUGEkVIMkU0b1ZX01ZDIUQ2Q0TEkkQSo0apQFcqASXwIVQT4VSCMVUUckTycVdYwzZDIULMYzXv.idUMiXD4DUzHzXYcFUXoTQwzjQMECUyPjLPMST4IVTYYEYvETah4zYCMkdyHjSRACUPQWUSUES3vFTz.0TjMSSpAEVMckVzTDQRcWVvvjaMYEV4IVaZQmY5AkbUkWTzbFaZk0YoQEVQYESGUjUMIURCkERznlVvzzZVwFNrM0byIEUEEUQRUURTAkcmYjVzj0UYMGMpUUREoVX5UELYETQoYUSEMTX3A0TgESUC4jQyQjUAkkQhoVQqMlPIIDRoUUahgWUrEld3.yX0kjLZ8FMwjUYYESXxEkUYgGLogTcTAiXqkjLhUmcVoUbUYTXuUDagUGTTkUdyYzX0EjLKwTQrgUcLQjVmAiUYIWUwDFc3TDU3gCaY81cVkUdIIDRqEkUZoGNrIVYvDSXpUkUOglKogjYLcjV0MlLLoFLogjcHIDRrgiQgoVUrI1TUYTXq0jQiUWRGI0ZqESVtE0UOgFQS0jcHIDRxUjQisFMwfEMvnWXpUkUOgFRCwjdlkFR4X2PTETRUAUSAIkVpASZHg1ZGI1YMIiXn4BZic1cVM1ZvjFR1MiPLg1Mn8zMtTETRUDUSYlZFkENHITXm81UjU1cwD1YQYkVzMFaHYFVWgkbUcUV3fjTLQmKogTcyLzSPUjZTEDLDgzaQY0SngzUYESUrIFZ3.SXzcmUjglKnM1Y2Y0XqASZHY2LBwDZ2f1S23RUPIUQTMkYpYTV3fDdhIGNFM1c2rFVm0jLhglKnM1Y2Y0XqASZHY2LBwDZ2f1S23RUPIUQTMkYpYTV3fDdhIGNFM1c2TTVq0jUXQSRBgTLEYTXvTkUOgFQCwjcyHDSncCZOciKUAkTEQ0TlolQYgCR3Ilb3XzX2cSQYg2ZxbkLUYzXn4BZic1cVM1ZvjFR24xPLQmKogTcyLzSPUjZTEDLDgzaQY0SnwzQgUWTWwTYmYkVscVLXASTsgjYXcEVxU0UYgCRnwjctLDS2MiPLg1Mn8zMtTETRUDUSYlZFkENHgmXxgiQic2MEEVciICVvDUaHYFVWgkbUcUV3fjPLQmKogTcyLzSPUjZTEDLDgzaQY0SnwzQgUWTWwTYvXEVwUkUiYGNvj0YqwVXn4BZic1cVM1ZvjFR1MiPNQiZS4DMpkVS2Y1TMkmKowjLLMTSncCZOciKUAkTEQ0TlolQYgCR3Ilb3XzX2cSQhgWUFk0Z2YEVzjjPHESQFEFLUY0Sn4RZKYGR3sTN1MDUAkTUP0TPRokZvjFR4cWLgoWQ4cUdQ0lXqEkLX4VRBgTLEYTXvTkUOglKosjcHg2R4X2PTETRUAUSAIkVpASZHk2cwDldEk2U5kzUYg1cVkEZtf1XmcmUisFLogjcyHDSncCZOciKUAkTEQ0TlolQYgCR3Ilb3XzX2cCLi8VTFMlaIIDRwTjQgASUV8DZtj1R1gDdKkic4szPmYEVyUkQgsFNrEVNt3hKt3hKt3hKt3hKtQUUCUEQTg2ZrM1YQcUVDUjQicVPP4RPHQEY1UTLhkWPP4RPL4hKi4hKt3hKt3hKtXlTU0DUQAURWoULEYzXqEEUXoWQFwyKIMzasA2atUlaz4COuX0TTMCTrU2Yo41TzEFck4C."
									}
,
									"fileref" : 									{
										"name" : "Chameleon",
										"filename" : "Chameleon.maxsnap",
										"filepath" : "~/Documents/Max 8/Snapshots",
										"filepos" : -1,
										"snapshotfileid" : "4913a32918dd4eba711ff5d40d73da46"
									}

								}
 ]
						}

					}
,
					"text" : "vst~",
					"varname" : "vst~",
					"viewvisibility" : 0
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"bgcolor" : [ 1.0, 0.788235, 0.470588, 1.0 ],
					"fontface" : 1,
					"fontsize" : 13.0,
					"hint" : "",
					"id" : "obj-35",
					"ignoreclick" : 1,
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 625.0, 404.0, 20.0, 20.0 ],
					"rounded" : 60.0,
					"text" : "1",
					"textcolor" : [ 0.34902, 0.34902, 0.34902, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"bgcolor" : [ 1.0, 0.788235, 0.470588, 1.0 ],
					"fontface" : 1,
					"hint" : "",
					"id" : "obj-11",
					"ignoreclick" : 1,
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 390.5, 451.5, 20.0, 20.0 ],
					"rounded" : 60.0,
					"text" : "3",
					"textcolor" : [ 0.34902, 0.34902, 0.34902, 1.0 ]
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-102", 1 ],
					"source" : [ "obj-100", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-102", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 1 ],
					"order" : 1,
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"order" : 2,
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"order" : 0,
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-99", 0 ],
					"source" : [ "obj-39", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-99", 0 ],
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-48", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-55", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-56", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-61", 0 ],
					"order" : 0,
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-87", 0 ],
					"order" : 1,
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"source" : [ "obj-61", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-63", 0 ],
					"source" : [ "obj-65", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-64", 0 ],
					"source" : [ "obj-65", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-61", 2 ],
					"source" : [ "obj-66", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 0 ],
					"source" : [ "obj-7", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-65", 0 ],
					"source" : [ "obj-7", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-102", 0 ],
					"order" : 1,
					"source" : [ "obj-87", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-99", 0 ],
					"order" : 0,
					"source" : [ "obj-87", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-100", 0 ],
					"order" : 1,
					"source" : [ "obj-99", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-114", 0 ],
					"order" : 0,
					"source" : [ "obj-99", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-7" : [ "vst~[3]", "vst~[3]", 0 ],
			"parameterbanks" : 			{

			}
,
			"inherited_shortname" : 1
		}
,
		"dependency_cache" : [ 			{
				"name" : "Chameleon.maxsnap",
				"bootpath" : "~/Documents/Max 8/Snapshots",
				"patcherrelativepath" : "../../../../Documents/Max 8/Snapshots",
				"type" : "mx@s",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}

}
