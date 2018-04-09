all_data = {
    "TOKEN": "508716388:AAGTPYwsumxdmWfuKLVPhFSK9ZpNRBeTIMY",
    "images": {
        "rip": {
            "mode": "bg",
            "path": "data/rip.png",
            "pos_to_paste": (55, 260),
            "paste_image_size": (330, 330)
        },
        "cancer": {
            "mode": "bg",
            "path": "data/cancer.jpg",
            "pos_to_paste": (345, 200),
            "paste_image_size": (110, 110)
        },
        "delete": {
            "mode": "bg",
            "path": "data/delete.png",
            "pos_to_paste": (115, 135),
            "paste_image_size": (185, 185)
        },

        "disabilities": {
            "mode": "bg",
            "path": "data/disabilities.jpg",
            "pos_to_paste": (470, 340),
            "paste_image_size": (165, 165)
        },
        "ban": {
            "mode": "bg",
            "path": "data/ban.png",
            "pos_to_paste": (115, 390),
            "paste_image_size": (300, 300)
        }
    },
    "geo_test": {
        "questions": [
            {
                "params": {
                    'l': 'sat',
                    'll': '94.110178,32.278826',
                    'z': '2',
                    'pt': '102.110178,32.278826,pm2vvm'
                },
                "question": "К какому континенту относится данная область?",
                "answers": [
                    "Индонезийскому",
                    "Азиатскому",
                    "Тихоокеанскому",
                    "Евразийскому"
                ],
                "true_answer": "Евразийскому"
            },
            {
                "params": {
                    'l': 'sat',
                    'll': '20.937475,2.927064999999999',
                    'z': '3',
                    'pt': '20.937475,6.927065,pm2vvm'
                },
                "question": "В каком направлении от данной точки находится ЮАР?",
                "answers": [
                    "Западном",
                    "Восточном",
                    "Южном",
                    "Северном"
                ],
                "true_answer": "Южном"

            },
            {
                "params": {
                    'l': 'sat',
                    'll': '32.376552,45.198308',
                    'z': '3',
                    'pt': '16.557649,35.760786,pm2rdm~'
                          '38.225849,19.996309,pm2gnm~'
                          '34.188335,43.229419,pm2blm~'
                          '19.908688,58.98793,pm2dom'
                },
                "question": "Какой метке соответствует Средиземное море?",
                "answers": [
                    "Зеленой",
                    "Красной",
                    "Синей",
                    "Оранжевой"
                ],
                "true_answer": "Красной"

            },
            {
                "params": {
                    'l': 'sat',
                    'll': '24.482771,53.02753',
                    'z': '3',
                    'pt': '31.482771,49.02753,pm2rdm~'
                          '19.758436,51.211428,pm2gnm~'
                          '28.030985,53.531205,pm2blm~'
                          '24.302788,45.942138,pm2dom'
                },
                "question": "Какой метке соответствует Украина?",
                "answers": [
                    "Зеленой",
                    "Красной",
                    "Синей",
                    "Оранжевой"
                ],
                "true_answer": "Красной"

            },
            {
                "params": {
                    'l': 'sat,skl',
                    'll': '41.622504,54.753215',
                    'z': '5',
                    'pt': '45.018316,53.195063,pm2ywm~'
                          '37.622504,55.753215,pm2ywm',
                    'pl': '45.018316,53.195063,37.622504,55.753215'
                },
                "question": "Какого расстояние от Пензы до Москвы?",
                "answers": [
                    "713 км",
                    "556 км",
                    "341 км",
                    "169 км"
                ],
                "true_answer": "556 км"

            },
            {
                "params": {
                    'l': 'sat,skl',
                    'll': '10.071148,52.324927',
                    'z': '4',
                    'pt': '-0.085708,51.511118,pm2rdm~'
                          '10.551692,51.228764,pm2gnm~'
                          '-8.448817,39.489874,pm2blm~'
                          '18.071148,59.324927,pm2dom'
                },
                "question": "Через какую из точек проходит нулевой мередиан?",
                "answers": [
                    "Зеленую",
                    "Красную",
                    "Синюю",
                    "Оранжевую"
                ],
                "true_answer": "Красную"

            },
            {
                "params": {
                    'l': 'sat',
                    'll': '30.315868,59.939095',
                    'z': '12',
                },
                "question": "Какой город изображен на картинке?",
                "answers": [
                    "Берлин",
                    "Лондон",
                    "Москва",
                    "Санкт-Петербург"
                ],
                "true_answer": "Санкт-Петербург"

            },
            {
                "params": {
                    'l': 'sat',
                    'll': '101.307704,16.378309',
                    'z': '4',
                    'pt': '101.307704,16.378309,pm2rdm'
                },
                "question": "Какая страна находится в отмеченной области?",
                "answers": [
                    "Китай",
                    "Мьянма",
                    "Таиланд",
                    "Индонезия"
                ],
                "true_answer": "Таиланд"

            },
            {
                "params": {
                    'l': 'sat',
                    'll': '-109.357714,-27.119532',
                    'z': '11',
                },
                "question": "Какой остров изображен на картинке?",
                "answers": [
                    "Гавайский",
                    "Пасхи",
                    "Самоа",
                    "Таити"
                ],
                "true_answer": "Пасхи"

            },
            {
                "params": {
                    'l': 'sat,skl',
                    'll': '17.45582,3.6580510000000004',
                    'z': '3',
                    'pt': '37.967861,0.399068,pm2rdm~'
                          '18.724699,15.339023,pm2gnm~'
                          '39.64463,8.582944,pm2blm~'
                          '17.45582,-12.341949,pm2dom'
                },
                "question": "Через какую из точек проходит экватор?",
                "answers": [
                    "Зеленую",
                    "Красную",
                    "Синюю",
                    "Оранжевую"
                ],
                "true_answer": "Красную"
            }
        ]
    }
}
