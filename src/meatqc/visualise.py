"""Draw ground-truth boxes on dataset images for visual inspection."""
import random
from pathlib import Path

import cv2

from inspect_data import load_class_names, read_labels


def draw_boxes(image, boxes, names):
    """Draw labelled rectangles on an image.

    Args:
        image: BGR image array (modified in place).
        boxes: List of (class_id, x_center, y_center, width, height),
            with coordinates normalised to 0-1.
        names: List of class names indexed by class id.

    Returns:
        The same image with boxes and class names drawn on it.
    """
    h, w = image.shape[:2]
    for cid, xc, yc, bw, bh in boxes:
        # convert normalised centre/size to pixel corner coordinates
        x1 = int((xc - bw / 2) * w)
        y1 = int((yc - bh / 2) * h)
        x2 = int((xc + bw / 2) * w)
        y2 = int((yc + bh / 2) * h)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, names[cid], (x1, max(y1 - 5, 12)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return image


def save_samples(root="data/raw", split="train", n=6, class_name=None,
                 seed=0, out_dir="results/figures/samples"):
    """Save randomly chosen annotated images to disk.

    Args:
        root: Dataset folder containing ``data.yaml`` and the split folders.
        split: Which split to sample from.
        n: Number of images to save.
        class_name: If given, only images containing this class are used.
        seed: Random seed, so the same images are chosen every run.
        out_dir: Folder the annotated images are written to.

    Returns:
        None. Images are written to ``out_dir``.
    """
    root = Path(root)
    names = load_class_names(root)
    img_dir = root / split / "images"
    lbl_dir = root / split / "labels"
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    candidates = []
    for img in sorted(img_dir.glob("*.jpg")):
        boxes = read_labels(lbl_dir / f"{img.stem}.txt")
        if not boxes:
            continue
        if class_name and class_name not in [names[b[0]] for b in boxes]:
            continue
        candidates.append((img, boxes))

    random.Random(seed).shuffle(candidates)
    for img_path, boxes in candidates[:n]:
        image = cv2.imread(str(img_path))
        cv2.imwrite(str(out_dir / img_path.name),
                    draw_boxes(image, boxes, names))
    print(f"{class_name}: saved {min(n, len(candidates))} images to {out_dir}")


if __name__ == "__main__":
    for cls in load_class_names("data/raw"):
        save_samples(class_name=cls, n=6, out_dir=f"results/figures/samples/{cls}")