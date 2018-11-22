Install dev project
---

**If you have already installed project**

Run microservises

```chmod +x up_microservises.sh```

```./up_microservises.sh```

Activate venv 

for Linux

```source venv/bin/activate```

for Windows

```source venv/Scripts/activate```


Run loader

```python balancer.py```

**else**

*You can use set_up.sh*

```chmod +x set_up.sh```

```./set_up.sh```

*or install manually*

Install PIP

```curl https://bootstrap.pypa.io/get-pip.py | python```

Create venv

```python -m virtualenv venv```

Activate venv 

for Linux

```source venv/bin/activate```

for Windows

```source venv/Scripts/activate```

Install dependencies

```pip install -r requirements.txt```
