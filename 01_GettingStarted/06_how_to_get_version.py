import subprocess

def get_tool_version(tool_name):
    try:
        # Run the tool command with the --version option
        result = subprocess.run([tool_name, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Parse the version information from the output
            version_info = result.stdout.strip()
            return f"{tool_name} version: {version_info}"
        else:
            # If the command failed, print the error message
            return f"Error: {result.stderr.strip()}"

    except Exception as e:
        # Handle exceptions, if any
        return f"An error occurred: {str(e)}"

# Example usage
tool_name = 'docker'
version_result = get_tool_version(tool_name)
print(version_result)