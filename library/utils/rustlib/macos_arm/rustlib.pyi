class LZ4ChainDecoder:
    def __del__(self, /): ...

    @classmethod
    def __new__(cls, *args, **kwargs): ...

    def decompress(self, /, src, block_size): ...


class Vpk:
    @classmethod
    def __new__(cls, *args, **kwargs): ...

    def find_file(self, /, path): ...

    @classmethod
    def from_path(cls, path): ...

    def glob(self, /, pattern): ...


__doc__: str
__file__: str
__name__: str
__package__: str


def decode_index_buffer(input_data, index_size, index_count): ...


def decode_texture(data, width, height, format): ...


def decode_vertex_buffer(input_data, vertex_size, vertex_count): ...


def encode_exr(pixel_data, width, height): ...


def encode_png(pixel_data, width, height): ...


def load_vtf_texture(vtf_data): ...


def lz4_compress(input_data): ...


def lz4_decompress(input_data, decompressed_size): ...


def save_exr(pixel_data, width, height, path): ...


def save_png(pixel_data, width, height, path): ...


def save_vtf_texture(output_path, width, height, format, generate_mips, resize, version, resize_size, pixel_data): ...


def zstd_compress(input_data): ...


def zstd_compress_stream(input_data): ...


def zstd_decompress(input_data, decompressed_size): ...


def zstd_decompress_stream(input_data): ...
