# test-dh-docker-vscode
Example of using Deephaven + Docker + VS Code for remote running debugging

## VS Code devcontainer

It is possible to use VS Code devcontainers to create a standard development environment 
for all developers on a project.  This development environment runs in a docker container.

To make this work:
1. Add keys in the terminal so that they are available in the devcontainer.
    ```bash
    ssh-add ~/.ssh/<github_key>
    ```
1. Check out the code:
    ```bash
    git@github.com:chipkent/test-dh-docker-vscode.git
    ````
1. Start vs code.
    ```bash
    code ./test-dh-docker-vscode
    ```
1. Click on the green `><` icon in the bottom left, and select `Open Folder in Container...`

Now, your VS Code development session will happen inside of a standardized container.

## Remote debugging

1. Run `docker compose up --build` from the console.
2. Launch `Python: Attach 10001` or `Python: Attach Host.Docker 10001` from the VS Code Run/Debug window.  The first probably works for Linux, and the second works for Mac.