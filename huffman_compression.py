import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, character=None, frequency=0):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def calculate_frequencies(data):
    frequencies = defaultdict(int)
    for character in data:
        frequencies[character] += 1
    return frequencies


def build_huffman_tree(frequencies):
    priority_queue = []
    for character, frequency in frequencies.items():
        heapq.heappush(priority_queue, HuffmanNode(character, frequency))

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(frequency=left_node.frequency + right_node.frequency)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def build_huffman_codes(huffman_tree):
    huffman_codes = {}

    def generate_codes(node, current_code):
        if node.character:
            huffman_codes[node.character] = current_code
            return

        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(huffman_tree, "")
    return huffman_codes


def compress_data(data):
    frequencies = calculate_frequencies(data)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = build_huffman_codes(huffman_tree)

    compressed_data = ""
    for character in data:
        compressed_data += huffman_codes[character]

    return compressed_data, huffman_tree


def decompress_data(compressed_data, huffman_tree):
    decompressed_data = ""
    current_node = huffman_tree

    for bit in compressed_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.character:
            decompressed_data += current_node.character
            current_node = huffman_tree

    return decompressed_data


# Example usage
data = "hello world"
compressed_data, huffman_tree = compress_data(data)
print("Compressed data:", compressed_data)

decompressed_data = decompress_data(compressed_data, huffman_tree)
print("Decompressed data:", decompressed_data)
