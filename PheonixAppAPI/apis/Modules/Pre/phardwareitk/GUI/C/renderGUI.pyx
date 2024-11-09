# render.pyx
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from sdl2 import SDL_GetError
import ctypes

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from Extentions import *

from math import *

# Utility function to set a color
def SetColor(Color color=Color(), float alpha=1.0):
    """
    Set the current OpenGL drawing color using RGBA values (0.0 to 1.0).
    """
    r, g, b = color.color
    glColor4f(r / 255.0, g / 255.0, b / 255.0, alpha)

def SetBackgroundColor(Color color=Color(), float alpha=1.0):
    """
    Set the background color for the OpenGL context.
    """
    glClearColor(color.color[0], color.color[1], color.color[2], alpha)  # Set clear color (background color)
    glClear(GL_COLOR_BUFFER_BIT)  # Apply the background color

def DrawRectangle(float x, float y, float width, float height, Color color=Color(), float alpha=1.0):
    """
    Draw a filled rectangle with the specified position, size, and color.
    """
    SetColor(color, alpha)
    
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def DrawLine(float x1, float y1, float x2, float y2, Color color=Color(), float alpha=1.0):
    """
    Draw a line between two points (x1, y1) and (x2, y2) with the specified color.
    """
    SetColor(color, alpha)
    
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def DrawCircle(float x, float y, float radius, int segments=36, Color color=Color(), float alpha=1.0):
    """
    Draw a filled circle at (x, y) with a given radius and color.
    """
    SetColor(color, alpha)
    
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Center of the circle
    for i in range(segments):
        angle = 2 * 3.14159 * i / segments  # Divide 360° into equal segments
        x_offset = radius * ctypes.c_float(cos(angle))
        y_offset = radius * ctypes.c_float(sin(angle))
        glVertex2f(x + x_offset, y + y_offset)
    glEnd()

def DrawText(float x, float y, str text, Color color=Color()):
    """
    Draw a string of text at position (x, y) with the specified color.
    Note: This requires SDL_ttf to be installed, so this is optional.
    """
    pass

def Render():
    """Renders Everything."""
    glFlush()

# Initialize OpenGL settings like the clear color and other states.
def Render_Initialize2D():
    """
    Initialize OpenGL settings for 2D rendering.
    """
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Default background color (black)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 800, 0, 600, -1, 1)  # Setup orthogonal projection (2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def renderTest1():
    """
    A placeholder render function that clears the screen and draws some shapes.
    You can customize this with your own shapes.
    """
    # Set the background color (optional: user-defined)
    SetBackgroundColor(color=Color("black"), alpha=1.0)

    # Draw a red rectangle
    DrawRectangle(100, 100, 200, 150, color=Color("black"), alpha=1.0)

    # Draw a blue circle
    DrawCircle(400, 300, 100, segments=36, color=Color("blue"), alpha=0.8)

    # Draw a white line
    DrawLine(50, 50, 750, 50, color=Color("white"), alpha=1.0)

    # DrawText(200, 500, "Hello, World!", color=Color("white"))

    Render()