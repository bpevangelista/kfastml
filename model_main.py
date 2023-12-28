import argparse

from kfastml.models.model_server_hf import ModelServerHF


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8080)
    args = parser.parse_args()
    return args


def model_main():
    args = handle_args()

    model_server = ModelServerHF(
        model_type='text-generation',
        model_uri='mistralai/Mistral-7B-v0.1',
        model_device='cuda:0',
        model_generation_params={
            'top_k': 30,
            'top_p': 0.9,
        }
    )
    model_server.run()


if __name__ == '__main__':
    model_main()