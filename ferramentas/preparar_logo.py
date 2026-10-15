#!/usr/bin/env python3
"""Prepara a logo de uma marca para o menu: corta a margem branca e deixa o fundo transparente.

Uso:
    python ferramentas/preparar_logo.py entrada.jpg assets/logo-marca.png

Precisa de: pip install pillow numpy

Depois, registre a logo no dicionário LOGOS de ferramentas/gerar.py e rode o gerador.
"""
import sys

import numpy as np
from PIL import Image


def cor_para_alpha(img, tolerancia=12.0):
    """Tira o fundo branco e mantém o suave das bordas (cor sobre branco -> cor com transparência)."""
    base = Image.new("RGB", img.size, (255, 255, 255))
    if img.mode == "RGBA":
        base.paste(img, mask=img.split()[3])
    else:
        base.paste(img.convert("RGB"))
    a = np.asarray(base).astype(np.float32)
    minimo = a.min(axis=2)
    alpha = np.clip((255.0 - minimo - tolerancia) / (255.0 - tolerancia), 0, 1)
    alpha_s = np.maximum(alpha, 1e-3)[..., None]
    cor = np.clip((a - 255.0 * (1 - alpha_s)) / alpha_s, 0, 255)
    return Image.fromarray(np.dstack([cor, alpha * 255.0]).astype(np.uint8), "RGBA")


def cortar(img, margem=6):
    alpha = np.asarray(img)[..., 3]
    ys, xs = np.where(alpha > 20)
    return img.crop((max(0, xs.min() - margem), max(0, ys.min() - margem),
                     min(img.width, xs.max() + margem + 1), min(img.height, ys.max() + margem + 1)))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    img = Image.open(sys.argv[1])
    saida = cortar(cor_para_alpha(img))
    saida.save(sys.argv[2], optimize=True)
    print(f"{sys.argv[2]}: {img.size} -> {saida.size}")


if __name__ == "__main__":
    main()
