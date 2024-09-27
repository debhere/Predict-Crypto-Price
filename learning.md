### How to activate virtual environment in Git Bash
1. Start Git bash and type conda. If the bash doesn't recognizde then conda is not activated.
```
conda
```
2. If 1. is true then search and navigate to /anaconda3/etc/profile.d in your program files
3. start Git Bash here and run the below command. This is to add the conda profile into your .bashrc file.

```
echo ". '${PWD}'/conda.sh" >> ~/.bashrc
```
4. Close Git Bash.
5. Move to your project folder and start Git Bash.
6. Type activate conda
```
activate conda
```
7. Now your should see (base) pop-up above your prompt.
8. Type in conda activate 'env-name' to activate your preferred virtual environment if already created
```
conda activate 'venv'
```