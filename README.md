# Full-Room

Developed by Gold's Gym Team:
- Adrian Wijaya (1806205363)
- Ari Angga Nugraha (1806205086)
- Christopher Samuel (180614115)
- Iqrar Agalosi Nureyza (1806204902)

# Installation Guide
1. Clone this repo.
```
git clone https://gitlab.com/iqrar99/full-room.git
```

2. Create virtual environment by using `venv` inside the repository.

On MacOs and Linux:
```
python3 -m venv env
```
On Windows:
```
python -m venv env
```
3. Activate the environment.

On MacOS and Linux:
```bash
source env/bin/activate
```

On Windows:
```
.\env\Scripts\activate
```

4. Install all the packages.
```
pip install -r requirements.txt
```

5. Inside the main module directory `fullroom` along the `settings.py`, create `.env` file and write your own Django secret key in it.
```
SECRET_KEY=YOUR_DJANGO_SECRET_KEY_HERE
```

6. Run the program.
```
python manage.py runserver
```