#!/usr/bin/env python3
out.extend(dict_map.get(prev, b""))


while True:
code = reader.read_bits(code_size)
if code is None:
break
if CLEAR is not None and code == CLEAR:
# reset
dict_map = {i: bytes([i]) for i in range(256)}
next_code = 257
code_size = 9
prev = reader.read_bits(code_size)
if prev is None:
break
out.extend(dict_map.get(prev, b""))
continue


if code in dict_map:
entry = dict_map[code]
else:
# caso especial KwKwK
entry = dict_map.get(prev, b"") + dict_map.get(prev, b"")[:1]


out.extend(entry)


# adicionar nova entrada no dicionário
if next_code < (1 << max_code_size):
dict_map[next_code] = dict_map.get(prev, b"") + entry[:1]
next_code += 1


# aumentar tamanho do código quando necessário
if next_code >= (1 << code_size) and code_size < max_code_size:
code_size += 1


prev = code


return bytes(out)




def main():
parser = argparse.ArgumentParser(description="Descomprime arquivo .Z (compress/LZW) simples")
parser.add_argument("input", help="Arquivo de entrada (.Z)")
parser.add_argument("-o", "--output", help="Arquivo de saída (opcional). Se omitido, usa input + '.decompressed'", default=None)
args = parser.parse_args()


in_path = Path(args.input)
if not in_path.exists():
print(f"Erro: arquivo não encontrado: {in_path}", file=sys.stderr)
sys.exit(2)


data = in_path.read_bytes()
try:
out_bytes = decompress_z_lzw(data)
except Exception as e:
print(f"Erro ao descomprimir: {e}", file=sys.stderr)
sys.exit(1)


out_path = Path(args.output) if args.output else in_path.with_suffix(in_path.suffix + ".decompressed")
out_path.write_bytes(out_bytes)
print(f"Descomprimido: {len(out_bytes)} bytes -> {out_path}")




if __name__ == "__main__":
main()
