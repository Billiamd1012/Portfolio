# Portfolio Flask App

A personal portfolio website built with Flask and Tailwind CSS.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

### Development
```bash
python main.py
```

### Production with Gunicorn

#### Option 1: Using the startup script
```bash
# Linux/Mac
chmod +x start.sh
./start.sh

# Windows
start.bat
```

#### Option 2: Direct Gunicorn command
```bash
gunicorn -c gunicorn.conf.py main:app
```

#### Option 3: Simple Gunicorn command
```bash
gunicorn main:app --bind 0.0.0.0:8000 --workers 4
```

## Configuration

The `gunicorn.conf.py` file contains production-ready settings:
- Binds to port 8000
- Uses multiple worker processes based on CPU cores
- Includes logging configuration
- Memory leak prevention with worker recycling

## Systemd Service (Linux)

To run as a system service:

1. Copy `portfolio.service` to `/etc/systemd/system/`
2. Update the paths in the service file
3. Enable and start the service:
```bash
sudo systemctl enable portfolio
sudo systemctl start portfolio
```

## Access

Once running, the app will be available at:
- Development: http://localhost:5000
- Production: http://localhost:8000

## Notes

- The app serves static files from the `static/` directory
- Experience data is loaded from `experience.json`
- Resume PDF should be placed in `static/dist/pdf/resume.pdf` 