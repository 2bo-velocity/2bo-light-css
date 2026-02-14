import re
import os

def minify_css(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    
    # Remove whitespace
    css = re.sub(r'\s+', ' ', css) # Replace multiple spaces/newlines with single space
    css = re.sub(r'\s*([:;{}])\s*', r'\1', css) # Remove space around colons, semis, braces
    css = css.replace(';}', '}') # Remove last semicolon
    css = css.strip()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(css)

    original_size = os.path.getsize(input_path)
    minified_size = os.path.getsize(output_path)
    
    print(f"Minified {input_path} -> {output_path}")
    print(f"Original size: {original_size} bytes")
    print(f"Minified size: {minified_size} bytes")

    if minified_size > 5120:
        print("WARNING: Minified size exceeds 5KB!")
    else:
        print("SUCCESS: Size is within 5KB limit.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, 'dist', '2boLight.css')
    output_file = os.path.join(base_dir, 'dist', '2boLight.min.css')
    
    minify_css(input_file, output_file)
