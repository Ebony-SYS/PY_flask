from flask.views import MethodView

class NaoEncontrado(MethodView):
    
    def get(self, error):
        return f"Página não encontrada {error}"