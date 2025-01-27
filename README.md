
# YouTube Video Downloader using Python, Flask, Bootstrap, and Pytube

This repository contains a web application for downloading YouTube videos using Python, Flask, Bootstrap, and the Pytube library.

## Getting Started

### Prerequisites
- Python installed on your machine.
- Flask installed.
- Pytube library installed.
- Bootstrap for styling the web application.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/nileshdeshmukh-code/online-video-downloader.git
   ```

2. Navigate to the project directory:
   ```
   cd YouTubeDownloader
   ```

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```
   pip install Flask pytube
   ```


## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter the URL of the YouTube video you want to download and click the "Download" button.

## Sample Code

### `app.py`
```python
from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download('downloads/')
    return send_file(os.path.join('downloads', stream.default_filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Video Downloader</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">YouTube Video Downloader</h1>
        <form method="post" action="/download">
            <div class="form-group">
                <label for="url">YouTube URL</label>
                <input type="text" class="form-control" id="url" name="url" placeholder="Enter YouTube URL" required>
            </div>
            <button type="submit" class="btn btn-primary">Download</button>
        </form>
    </div>
</body>
</html>
```

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pytube Documentation](https://pytube.io/)
- [Bootstrap Documentation](https://getbootstrap.com/)
```

You can now copy and paste this entire block directly into your `README.md` file for your YouTube video downloader project. Let me know if there's anything else you need! 😊
