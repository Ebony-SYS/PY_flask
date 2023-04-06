from src.controller.controller import *
from src.controller.erros import NaoEncontrado

routes = dict(
    home='/', test=TestConstroller.as_view('Testando'),
    notFound_route=404, ne=NaoEncontrado.as_view('Não encontrei a página.'),
)