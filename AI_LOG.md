\# AI Use Log



| Date | Tool | What I asked for | What I used | How I checked it | Errors / issues found |

|------|------|------------------|-------------|------------------|-----------------------|

| 2026-10-21 | Claude | Repo structure and setup steps | Folder layout, .gitignore advice, requirements list | Ran the commands, confirmed folders and install worked | Gave Mac/Linux commands first; they failed in Windows PowerShell and had to be redone after I noticed the mismatched language |
| 2026-10-21 | Claude | Find and download the Roboflow dataset, then write a script to inspect it | Download steps and a YOLO-format inspection script (`inspect\_data.py`) | Ran it, then checked that train + valid + test = 3,549 images, matching the project slide | First script I was given was generic and assumed no label format; it was replaced once the data turned out to be YOLO format |

| 2026-10-21 | Claude | Script to draw ground-truth boxes on sample images | `visualise.py` (box drawing and sampling) | Ran it, then checked by eye that boxes sit on the defects | 
| 2026-10-22 | Claude | Help narrow the project scope from my notes on the images and class counts | Recommended scope: detect `packaging-error` and `unsealed`, plus tray-level pass/fail; I chose this option | Checked the class counts myself: the other three classes have too few validation and test boxes to measure | |

| 2026-10-22 | Claude | Draft problem statement and inputs/outputs spec | Draft text, which I checked against what I saw and rewrote in my own words | Compared each claim with my image notes and the dataset page | \[write what you changed or corrected] |

| 2026-10-22 | Claude | Script to sample unlabelled images for a manual label audit | `audit\_empty.py` | Ran it and checked all sampled images by eye; extended it to the valid and test splits | |

