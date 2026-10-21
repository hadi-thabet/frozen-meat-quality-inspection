\# AI Use Log



| Date | Tool | What I asked for | What I used | How I checked it | Errors / issues found |

|------|------|------------------|-------------|------------------|-----------------------|

| 2026-10-21 | Claude | Repo structure and setup steps | Folder layout, .gitignore advice, requirements list | Ran the commands, confirmed folders and install worked | Gave Mac/Linux commands first; they failed in Windows PowerShell and had to be redone after I noticed the mismatched language |
| 2026-10-21 | Claude | Find and download the Roboflow dataset, then write a script to inspect it | Download steps and a YOLO-format inspection script (`inspect\_data.py`) | Ran it, then checked that train + valid + test = 3,549 images, matching the project slide | First script I was given was generic and assumed no label format; it was replaced once the data turned out to be YOLO format |

| 2026-10-21 | Claude | Script to draw ground-truth boxes on sample images | `visualise.py` (box drawing and sampling) | Ran it, then checked by eye that boxes sit on the defects | |

