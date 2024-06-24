import pytest
import requests


class TestYandexDisk:
    def setup_method(self):
        # Получите ЯДиск токен здесь: https://yandex.ru/dev/disk/poligon/
        token = ''
        self.headers = {
            'Authorization': f'OAuth {token}'
        }

    def teardown_method(self):
        params = {'path': 'Image'}
        requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                        headers=self.headers,
                        params=params)


    @pytest.mark.parametrize(
        'param,value,status',
        (
            ['path', 'Image', 201],
            ['pat', 'Image', 400]
        )
    )
    def test_create_folder(self, param, value, status):
        params = {param: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == status

    def test_double_create_folder(self):
        params = {'path': 'Image'}
        for _ in range(2):
            response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                    headers=self.headers,
                                    params=params)
        assert response.status_code == 409
