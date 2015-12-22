import web
import string
import datetime

render = web.template.render('templates/')


urls = (
	'/', 'index',
	'/button1', 'button1',
	'/button2', 'button2',
	'/button3', 'button3',
	'/button4', 'button4',
	'/button5', 'button5',
	'/button6', 'button6',
	'/button7', 'button7',
	'/button8', 'button8',
	'/button9', 'button9',
	'/button10', 'button10',
	'/button11', 'button11',
	'/button12', 'button12',		
	'/Trebound', 'Trebound',
	'/Drebound', 'Drebound',
	'/Orebound', 'Orebound',
	'/Assist', 'Assist',
	'/Turnover', 'Turnover',
	'/Block', 'Block',
	'/Fg', 'Fg',
	'/Fg3', 'Fg3',
	'/Ft', 'Ft',
	'/steal','steal',
	'/pf', 'pf',
	'/ov', 'ov',
	'/home', 'home'
	
)


class index:
	def GET(self):
		return render.index()

class button1:
	def POST(self):
		raise web.seeother('/Trebound')

class Trebound:
	def GET(self):
		return render.Trebound()

class button2:
	def POST(self):
		raise web.seeother('/Drebound')

class Drebound:
	def GET(self):
		return render.Drebound()

class button3:
	def POST(self):
		raise web.seeother('/Orebound')

class Orebound:
	def GET(self):
		return render.Orebound()

class button4:
	def POST(self):
		raise web.seeother('/Assist')

class Assist:
	def GET(self):
		return render.Assist()

class button5:
	def POST(self):
		raise web.seeother('/Turnover')

class Turnover:
	def GET(self):
		return render.Turnover()

class button6:
	def POST(self):
		raise web.seeother('/Block')

class Block:
	def GET(self):
		return render.Block()

class button7:
	def POST(self):
		raise web.seeother('/Fg')

class Fg:
	def GET(self):
		return render.Fg()

class button8:
	def POST(self):
		raise web.seeother('/Fg3')

class Fg3:
	def GET(self):
		return render.Fg3()

class button9:
	def POST(self):
		raise web.seeother('/Ft')

class Ft:
	def GET(self):
		return render.Ft()

class button10:
	def POST(self):
		raise web.seeother('/steal')

class steal:
	def GET(self):
		return render.steal()

class button11:
	def POST(self):
		raise web.seeother('/pf')

class pf:
	def GET(self):
		return render.pf()

class button12:
	def POST(self):
		raise web.seeother('/ov')

class ov:
	def GET(self):
		return render.ov()


class home:
	def POST(self):
		raise web.seeother('/')




		
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
