# tiwood.uz

This is the Flask web application for the website tiwood.uz.

## Project Structure

```
tiwood.uz
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates
│       └── index.html
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── script.js
│   └── images
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/tiwood.uz.git
   cd tiwood.uz
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:
```
flask run
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Contributing

Feel free to submit issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.