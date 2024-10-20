# Wrinkler AutoClicker

Wrinkler AutoClicker is a simple Python-based script that automates the task of clicking Wrinklers in the popular browser game *Cookie Clicker*. Wrinklers can accumulate over time, and popping them is an important way to boost your cookie production. With this script, you can set it up to click Wrinklers at predefined coordinates, so you can continue progressing in the game with minimal effort.

## Features

- **Auto-clicking of Wrinklers:** Automatically clicks on Wrinklers around the Big Cookie.
- **Easy-to-modify:** You can change the coordinates to suit your specific game screen setup.
- **Lightweight & Fast:** The script is designed to run in the background without affecting your game performance.

## Requirements

- Python 3.x
- `pyautogui` package for automating mouse clicks
- `time` package (part of Python Standard Library)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Wrinkler-AutoClicker.git
    cd Wrinkler-AutoClicker
    ```

2. Install dependencies:
    ```bash
    pip install pyautogui
    ```

## Usage

1. **Change Coordinates**: Update the `coords` variable in the script with your game's Wrinkler positions.

   You can easily find your Wrinkler coordinates by using a tool like [https://www.colorzilla.com/](https://www.colorzilla.com/) (which provides x/y positions of your mouse cursor). Open Cookie Clicker, hover over the Wrinklers, and note down the x/y values.

   Open the script (`wrinkler_clicker.py`) and update the coordinates like this:

    ```python
    coords = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]  # Add coordinates for all 6 Wrinklers
    ```

2. **Run the Script**: Once you've set the coordinates, run the script.
    ```bash
    python wrinkler_clicker.py
    ```

   The script will now automatically click on the specified Wrinkler coordinates at regular intervals.

## How to Get Coordinates

1. Open Cookie Clicker in your browser and zoom in/out until Wrinklers are visible clearly.
2. Use a tool like ColorZilla to get the x and y coordinates for each Wrinkler.
3. Update the script with these new coordinates.

## Contributing

Contributions are welcome! If you find bugs or have suggestions for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

