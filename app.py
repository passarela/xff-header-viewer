from flask import Flask, request
import datetime

app = Flask(__name__)
logs = []

@app.before_request
def log_request():
    forwarded_for = request.headers.get('X-Forwarded-For')
    x_real = request.headers.get('X-Real-IP')
    remote_addr = request.remote_addr
    client_ip = request.headers.get('CLIENTIP')
    agent = request.headers.get('User-Agent')
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logs.append({'X-Forwarded-For': forwarded_for,'X-Real-IP': x_real, 'remote_addr': remote_addr, 'CLIENTIP': client_ip, 'agent': agent, 'date_time': date_time})

@app.route('/')
def show_logs():
    html = '<h1>Logs de Acesso</h1>'
    html += '<table>'
    html += '<tr><th>X-Forwarded-For</th><th>X-Real-IP</th><th>remote_addr</th><th>CLIENTIP</th><th>Agent</th><th>Data/Hora</th></tr>'
    for log in logs:
        html += f'<tr><td>{log["X-Forwarded-For"]}</td><td>{log["X-Real-IP"]}</td><td>{log["remote_addr"]}</td><td>{log["CLIENTIP"]}</td><td>{log["agent"]}</td><td>{log["date_time"]}</td></tr>'
    html += '</table>'
    html += '<style>'
    html += 'table {border-collapse: collapse; width: 100%;}'
    html += 'th, td {padding: 8px; text-align: left; border-bottom: 1px solid #ddd;}'
    html += 'tr:hover {background-color:#f5f5f5;}'
    html += 'th {background-color: #4CAF50; color: white;}'
    html += '</style>'
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
