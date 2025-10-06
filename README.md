# descomprimir-arquivos-no-formato-Unix
aqui estão dois arquivos prontos para você salvar e enviar ao seu repositório:  decompress_z_lzw.py — script Python que descomprime arquivos no formato Unix compress (.Z / LZW).  README.txt — instruções e exemplos de uso, informações de segurança e licenças.

Decompressor .Z (compress / LZW)


Arquivos incluídos:
- decompress_z_lzw.py -> Script Python para descompressão de arquivos Unix .Z


Descrição:
Este pequeno utilitário implementa um decodificador LZW compatível com o formato "compress" da família Unix (arquivos .Z, header 0x1F 0x9D). O script é intencionalmente simples e educacional — ideal para CTFs, laboratórios e uso forense com permissão.


Requisitos:
- Python 3.8 ou superior


Uso:
1) Tornar executável (opcional):
chmod +x decompress_z_lzw.py


2) Executar:
python3 decompress_z_lzw.py arquivo_input.Z
# ou
./decompress_z_lzw.py arquivo_input.Z -o saida.bin


O script grava o conteúdo descomprimido no arquivo indicado. Se -o não for usado, grava em: arquivo_input.Z.decompressed


Avisos de segurança e ética:
- Só use este script em arquivos que você tem permissão explícita para analisar (CTF/lab/forense com autorização).
- Não utilize essas técnicas para acessar dados alheios sem consentimento.


Como subir no GitHub (rápido):
1) Crie um novo repositório no GitHub.
2) No seu repositório local:
git init
git add decompress_z_lzw.py README.txt
git commit -m "Add LZW .Z decompressor and README"
git branch -M main
git remote add origin <URL-do-repo>
git push -u origin main


Licença:
MIT License — sinta-se livre para adaptar.
