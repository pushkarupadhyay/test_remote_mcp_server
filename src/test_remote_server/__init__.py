from fastmcp import FastMCP
import random
import json

#crete a FastMCP server instance
mcp=FastMCP("simple calculcator server")

#tool: Add two numbers

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """add two numbers together"""

    """Args:
        a:First number
        b: second number
    Returns:
        The sum of a and b
        """
    return a + b

#tool: Genrate a random number

@mcp.tool()
def random_number(min_val: int = 1, max_val: int=100) -> int:
    """Generate a random number between min_val and max_val"""

    """Args:
        min_val: minimum value of the random number
        max_val: maximum value of the random number
    Returns:
        A random number between min_val and max_val
        """
    return random.randint(min_val, max_val)

#resource: Get server information

@mcp.resource("info://server")
def get_server_info() -> str:
    """Get server information"""
    info ={
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A simple calculator server that can add numbers and generate random numbers.",
        "tools":["add","random_number"],
        "authors":"Pushkar Upadhyay"

    }
    return json.dumps(info, indent=4)

#start the server
if __name__ == "__main__":
    # mcp.run()   then this mean we are selecting STDIO transport and default host and port and done in local server mcp
    mcp.run(transport="http", host="0.0.0.0", port=8000)