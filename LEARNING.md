## How to activate virtual environment in Git Bash

1. Start Git bash and type conda. If the bash doesn't recognizde then conda is not activated.

```bash
conda
```
2. If 1. is true then search and navigate to /anaconda3/etc/profile.d in your program files

3. start Git Bash here and run the below command. This is to add the conda profile into your .bashrc file.

```bash
echo ". '${PWD}'/conda.sh" >> ~/.bashrc
```
4. Close Git Bash.

5. Move to your project folder and start Git Bash.

6. Type activate conda

```bash
activate conda
```
7. Now you should see (base) pop-up above your prompt.

8. Type in conda activate 'env-name' to activate your preferred virtual environment if already created

```bash
conda activate 'venv'
```

## Streamlit

1. Realized that a stream object (write_stream) gets the app automatically refreshed.

## Misclaneous

1. You cannot invoke a module without installation if both are not having same parent directory.
2. Numeric arguments in fire automatically gets converted into integer. Consider the below example for command line argument. "19660423" is automatically convereted to integer by fire.

```bash
python hello.py "19660423"

```
3. use the full path while removing an environment if you have multiple environments with the same name.

```bash

conda env remove -p "[FULL PATH]"

```
4. If exists remove setup.py else pyproject.toml file will not work



