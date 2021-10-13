# nz-weather
For a live build, visit - https://brandonru.pythonanywhere.com/<br>
NZ Openweather API data rendered using Django3 and requests ☀️ 


## Local Run Instructions
First, clone into the git repository <code>git clone https://github.com/brandiny/nz-weather</code> and setup the virtual environment.

<table>
    <tr>
        <td>Windows</td>
        <td><code>py -m venv env && env\Scripts\activate && py -m pip install -r requirements.txt</code></td>
    </tr>
    <tr>
        <td>Linux</td>
        <td><code>python3 -m venv env && source env/bin/activate && pip3 install -r requirements.txt</code></td>
    </tr>
</table>

With Python3 installed, cd into the src/weatherchallenge directory and run these commands
<table>
    <tr>
        <td>Windows & Linux</td>
        <td><code>python3 manage.py runserver</code></td>
    </tr>
</table>

The website will be hosted locally at http://127.0.0.1:8000/
