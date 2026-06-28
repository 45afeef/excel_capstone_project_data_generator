1. Running the Interactive Container
You must use the -it flags with docker run:

-i (interactive): Keeps STDIN open so you can type commands. 
-t (tty): Allocates a pseudo-terminal for proper formatting and signal handling (like Ctrl+C). 
```
docker build -t my-python-cli .
docker run -it --rm my-python-cli
```
Once inside, you have a full shell where you can run python, pip, or any installed CLI tool live. 