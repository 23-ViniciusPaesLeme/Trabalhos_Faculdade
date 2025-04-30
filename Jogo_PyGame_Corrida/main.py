import pygame
from pygame.locals import *
import random

# Definindo as classes de veículos fora do método __init__()
class Veiculo(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y):
        pygame.sprite.Sprite.__init__(self)

        escala_imagem = 45 / imagem.get_rect().width
        nova_largura = imagem.get_rect().width * escala_imagem
        nova_altura = imagem.get_rect().height * escala_imagem
        self.image = pygame.transform.scale(imagem, (nova_largura, nova_altura))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class VeiculoJogador(Veiculo):
    def __init__(self, x, y):
        imagem = pygame.image.load('assets/carro.png')
        super().__init__(imagem, x, y)
        self.imagem = imagem

class Jogo:
    def __init__(self):
        pygame.init()

        self.largura = 500
        self.altura = 500
        self.tamanho_tela = (self.largura, self.altura)
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        pygame.display.set_caption("Jogo de corrida")

        self.cinza = (100, 100, 100)
        self.verde = (76, 208, 56)
        self.branco = (255, 255, 255)
        self.vermelho = (200, 0, 0)

        self.largura_estrada = 300
        self.largura_marcador = 10
        self.altura_marcador = 40

        self.faixa_esquerda = 150
        self.faixa_central = 250
        self.faixa_direita = 350
        self.faixas = [self.faixa_esquerda, self.faixa_central, self.faixa_direita]

        self.estrada = (100, 0, self.largura_estrada, self.altura)
        self.marcador_borda_esquerda = (95, 0, self.largura_marcador, self.altura)
        self.marcador_borda_direita = (395, 0, self.largura_marcador, self.altura)

        self.movimento_marcador_faixa_y = 0

        self.x_jogador = 250
        self.y_jogador = 400

        self.relogio = pygame.time.Clock()
        self.fps = 120
        self.velocidade = 2
        self.pontos = 0

        # Inicializando grupos de sprites
        self.grupo_jogador = pygame.sprite.Group()
        self.grupo_veiculos = pygame.sprite.Group()

        # Criando o jogador
        self.jogador = VeiculoJogador(self.x_jogador, self.y_jogador)
        self.grupo_jogador.add(self.jogador)

        # Carregando imagens de veículos
        self.arquivos_imagens = ['caminhao.png', 'caminhonete.png', 'taxi.png', 'van.png']
        self.imagens_veiculos = []
        for arquivo_imagem in self.arquivos_imagens:
            imagem = pygame.image.load('assets/' + arquivo_imagem)
            self.imagens_veiculos.append(imagem)

        # Imagem de colisão
        self.colisao = pygame.image.load('assets/colisao.png')
        self.rect_colisao = self.colisao.get_rect()

        # Variáveis de controle
        self.fim_jogo = False

    def loop(self):
        rodando = True
        while rodando:
            self.relogio.tick(self.fps)

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    rodando = False

                if evento.type == KEYDOWN:
                    if evento.key == K_LEFT and self.jogador.rect.center[0] > self.faixa_esquerda:
                        self.jogador.rect.x -= 100
                    elif evento.key == K_RIGHT and self.jogador.rect.center[0] < self.faixa_direita:
                        self.jogador.rect.x += 100

            # Verificando colisões
            if pygame.sprite.spritecollide(self.jogador, self.grupo_veiculos, True):
                self.fim_jogo = True

            # Atualizando a tela
            self.tela.fill(self.verde)
            pygame.draw.rect(self.tela, self.cinza, self.estrada)
            pygame.draw.rect(self.tela, self.branco, self.marcador_borda_esquerda)
            pygame.draw.rect(self.tela, self.branco, self.marcador_borda_direita)

            # Movimento das faixas
            self.movimento_marcador_faixa_y += self.velocidade * 2
            if self.movimento_marcador_faixa_y >= self.altura_marcador * 2:
                self.movimento_marcador_faixa_y = 0
            for y in range(self.altura_marcador * -2, self.altura, self.altura_marcador * 2):
                pygame.draw.rect(self.tela, self.branco, (self.faixa_esquerda + 45, y + self.movimento_marcador_faixa_y, self.largura_marcador, self.altura_marcador))
                pygame.draw.rect(self.tela, self.branco, (self.faixa_central + 45, y + self.movimento_marcador_faixa_y, self.largura_marcador, self.altura_marcador))

            self.grupo_jogador.draw(self.tela)

            # Gerando veículos inimigos
            if len(self.grupo_veiculos) < 2:
                adicionar_veiculo = True
                for veiculo in self.grupo_veiculos:
                    if veiculo.rect.top < veiculo.rect.height * 1.5:
                        adicionar_veiculo = False
                if adicionar_veiculo:
                    faixa = random.choice(self.faixas)
                    imagem = random.choice(self.imagens_veiculos)
                    veiculo = Veiculo(imagem, faixa, -50)
                    self.grupo_veiculos.add(veiculo)

            # Movendo os veículos
            for veiculo in self.grupo_veiculos:
                veiculo.rect.y += self.velocidade
                if veiculo.rect.top >= self.altura:
                    veiculo.kill()
                    self.pontos += 1
                    if self.pontos > 0 and self.pontos % 5 == 0:
                        self.velocidade += 1

            self.grupo_veiculos.draw(self.tela)

            # Exibindo pontos
            fonte = pygame.font.Font(pygame.font.get_default_font(), 16)
            texto = fonte.render('Pontos: ' + str(self.pontos), True, self.branco)
            texto_rect = texto.get_rect()
            texto_rect.center = (50, 400)
            self.tela.blit(texto, texto_rect)

            # Verificando fim de jogo
            if self.fim_jogo:
                self.tela.blit(self.colisao, self.rect_colisao)
                pygame.draw.rect(self.tela, self.vermelho, (0, 50, self.largura, 100))
                fonte = pygame.font.Font(pygame.font.get_default_font(), 16)
                texto = fonte.render('Fim de jogo. Jogar novamente? (Pressione Y ou N)', True, self.branco)
                texto_rect = texto.get_rect()
                texto_rect.center = (self.largura / 2, 100)
                self.tela.blit(texto, texto_rect)

            pygame.display.update()

            # Fim de jogo - Reiniciar ou Sair
            while self.fim_jogo:
                self.relogio.tick(self.fps)

                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        self.fim_jogo = False
                        rodando = False

                    if evento.type == KEYDOWN:
                        if evento.key == K_y:
                            self.fim_jogo = False
                            self.velocidade = 2
                            self.pontos = 0
                            self.grupo_veiculos.empty()
                            self.jogador.rect.center = [self.x_jogador, self.y_jogador]
                        elif evento.key == K_n:
                            self.fim_jogo = False
                            rodando = False

        pygame.quit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.loop()
