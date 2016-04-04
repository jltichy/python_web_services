#!/usr/bin/env python

import web

db = web.database(dbn='postgres', user='username', pw='password', db='dbname')

CREATE TABLE todo (
  id serial primary key,
  title text,
  created timestamp default now(),
  done boolean default 'f'    );
  
INSERT INTO todo (title) VALUES ('Learn web.py');

def GET(self):
    todos = db.select('todo')
    return render.index(todos)
    
'/', 'index',

$def with (todos)
<ul>
$for todo in todos:
    <li id="t$todo.id">$todo.title</li>
</ul>

<form method="post" action="add">
<p><input type="text" name="title" /> <input type="submit" value="Add" /></p>
</form>

'/', 'index',
'/add', 'add'

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')
        
post_data=web.input(name=[])
