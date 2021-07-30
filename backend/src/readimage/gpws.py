import cherrypy
import gpprocessor
import json

p = gpprocessor.GPProcessor()

class GPWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def process(self):
      data = cherrypy.request.json
      output = p.run(data)
      return json.dumps(output, indent=2)

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(GPWebService())
