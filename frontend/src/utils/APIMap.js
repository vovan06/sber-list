const server_domain = 'http://alexander.kizimenko.fvds.ru/api/v1/docs/';

const api_paths = {
    register: server_domain + 'auth/register/',
    login: server_domain + 'auth/login/',
    token_pair: server_domain + 'token/',
    token_veify: server_domain + 'token/verify/',
    token_refresh: server_domain + 'token/refresh/',
};

export default api_paths;