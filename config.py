import os

class Config:
    # Configurações gerais
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    DEBUG = False
    BEARER_TOKEN = os.getenv('BEARER_TOKEN', 'your-bearer-token-here')
    
    # Configurações por marca

    
    FONT_PATH = {'brand_b': 'static/brands/brand-b/fonts/CircularStd-Bold.otf', 
                 'brand_c': 'static/brands/brand-c/fonts/Decoy-Black.otf',
                 'brand_a': 'static/brands/brand-a/fonts/Bison-Bold.ttf'}
    
    LOGOS_PATH = {'brand_b': 'static/brands/brand-b/logos/',
                 'brand_c': 'static/brands/brand-c/logos/',
                 'brand_a': 'static/brands/brand-a/logos/'}
    
    VIDEOS_PATH = {'brand_b': 'static/brands/brand-b/videos/',
                 'brand_c': 'static/brands/brand-c/videos/',
                 'brand_a': 'static/brands/brand-a/videos/'}
    
    FUNDO_IMAGEM_PATH = {'brand_b': 'static/brands/brand-b/frames/fundo_lct.jpeg',
                 'brand_c': 'static/brands/brand-c/frames/fundo_bdc.jpeg',
                 'brand_a': 'static/brands/brand-a/frames/fundo_crn.jpeg'}
    
    IMAGEM_FINAL_PATH = {'brand_b': 'static/brands/brand-b/frames/baseplate_lct.jpeg',
                 'brand_c': 'static/brands/brand-c/frames/baseplate_bdc.jpeg',
                 'brand_a': 'static/brands/brand-a/frames/baseplate_crn.jpeg'}

    BOTTOM_IMAGEM_PATH = {'brand_b': 'static/brands/brand-b/bottom/bottom_lct.jpeg',
                 'brand_c': 'static/brands/brand-c/bottom/bottom_bdc.jpeg',
                 'brand_a': 'static/brands/brand-a/bottom/bottom_crn.png'}
    
    BG_VIDEO_PATH = {'brand_b': 'static/brands/brand-b/frames/bg_lacta.mp4',
                 'brand_c': 'static/brands/brand-c/frames/bg_bauducco.mp4',
                 'brand_a': 'static/brands/brand-a/frames/bg_sea.mp4'}
    
    BG_VIDEO_LOGO_PATH = {'brand_b': 'static/brands/brand-b/frames/bg_lacta_logo.mp4',
                'brand_c': 'static/brands/brand-c/frames/bg_bauducco_logo.mp4',
                'brand_a': 'static/brands/brand-a/frames/bg_clip_logo.mp4'}
    
    TARGET_PATH = {'brand_b': 'static/brands/brand-b/target/',
                'brand_c': 'static/brands/brand-c/target/',
                'brand_a': 'static/brands/brand-a/target/'}

    # Arquivos compartilhados
    WEATHER_JSON = 'static/data/weather-cd.json'
    AVALIACOES_PATH = 'static/data/avaliacoes.json'
    ENVIROMENT_DATA = 'static/data/env_variables.json'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}