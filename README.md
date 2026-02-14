# 2bo Light CSS

**2bo (Small. Fast. Reliable.)**
"Write HTML. Looks decent."

**2bo Light CSS** is a simple, lightweight modern CSS framework designed to make plain HTML look great without the hassle.

- **Size**: < 3KB (Minified)

## Features

- **Extremely Lightweight**: Currently ~2.3KB (minified). Pure CSS, no bloat.
- **Intuitive Class Names**: Simple, descriptive names like `.container`, `.flex`, `.text-center`.
- **Modern CSS Only**: Built for modern browsers using standard CSS features.
- **No Build Tools Required**: Just drop the `.css` file in and go. No SCSS, no Node.js required for usage.
- **Ready to Use**: Instant styling for basic HTML elements.

## Installation

### Download

Download the latest version from the `dist` folder:

- [2boLight.min.css](dist/2boLight.min.css) (Production)
- [2boLight.css](dist/2boLight.css) (Development)

### HTML Usage

Add the stylesheet to your `<head>`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Simple Site</title>
    <link rel="stylesheet" href="path/to/2boLight.min.css">
</head>
<body>
    <div class="container">
        <h1>Hello, World!</h1>
        <p>This is a simple page using 2bo Light CSS.</p>
        <button class="btn">Get Started</button>
    </div>
</body>
</html>
```

## Customization (CSS Variables)

You can easily customize the look and feel by overriding the CSS variables:

```css
:root {
  --space: 8px;           /* Base spacing unit */
  --radius: 8px;          /* Border radius */
  --color-text: #222;     /* Text color */
  --color-bg: #fff;       /* Background color */
  --color-main: #2563eb;  /* Primary color (Blue) */
  --color-border: #e5e7eb;/* Border color */
}
```

## Class Reference

### Layout

| Class | Description |
|-------|-------------|
| `.container` | Centered container with max-width 1100px. |
| `.flex` | `display: flex` |
| `.flex-col` | Flex column direction. |
| `.row` | Flex row direction. |
| `.center` | Flexbox centering (both axes). |
| `.w-full` | Width 100%. |

### Spacing

- **Margin**: `.m0` (0), `.m1` (4px), `.m2` (8px), `.m3` (16px)
- **Padding**: `.p0` (0), `.p1` (4px), `.p2` (8px), `.p3` (16px)

### Typography

- **Size**: `.text-sm` (small), `.text-md` (medium), `.text-lg` (large)
- **Alignment**: `.text-left`, `.text-center`, `.text-right`

### Components

#### Buttons
- `.btn` or `.btn-primary`: Default primary button.
- `.btn-outline`: Outline style button.
- `.btn-ghost`: Transparent background button.

#### Forms
- `.input`: Full-width text input.
- `.select`: Full-width select box.
- `.checkbox`: Auto-width checkbox.
- `.label`: Block label with bottom margin.

## Browser Support

Designed for **modern browsers only**:
- Google Chrome (Latest)
- Mozilla Firefox (Latest)
- Microsoft Edge (Latest)
- Safari (Latest)

Legacy browsers (IE11, older versions) are **not** supported.

## Development

If you want to contribute or modify the source:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/2bo-light-css.git
   ```

2. **Modify CSS**:
   Edit `dist/2boLight.css`.

3. **Minify (Build)**:
   Run the included Python script to generate the minified version.
   ```bash
   python3 scripts/build.py
   ```

4. **Verify**:
   Open `test/index.html` in your browser to check changes.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

**Author:** [2bo](https://github.com/2bo-velocity)
**Copyright:** (c) 2026 2bo

