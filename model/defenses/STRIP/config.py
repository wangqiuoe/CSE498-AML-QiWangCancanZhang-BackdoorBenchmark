import argparse

PREFIX = '/home/jupyter-caz322/lehigh_courses/DSCI_498/AMLproject/'

def get_argument():
    parser = argparse.ArgumentParser()

    # Directory option
    parser.add_argument("--data_root", type=str, default="/home/ubuntu/temps")
    parser.add_argument("--checkpoints", type=str, default="../../checkpoints")
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--results", type=str, default="./results")
    parser.add_argument("--dataset", type=str, default="cifar10")
    parser.add_argument("--attack_mode", type=str, default="all2one")
    parser.add_argument("--attack", type=str, default="wanet")
    parser.add_argument("--temps", type=str, default="./temps")

    # ---------------------------- For Neural Cleanse --------------------------
    # Model hyperparameters
    parser.add_argument("--n_sample", type=int, default=100)
    parser.add_argument("--n_test", type=int, default=100)
    parser.add_argument("--detection_boundary", type=float, default=0.2)  # According to the original paper
    parser.add_argument("--num_workers", type=int, default=2)
    parser.add_argument("--test_rounds", type=int, default=10)

    parser.add_argument("--s", type=float, default=0.5)
    parser.add_argument("--k", type=int, default=4)  # low-res grid size
    parser.add_argument(
        "--grid-rescale", type=float, default=1
    )  # scale grid values to avoid going out of [-1, 1]. For example, grid-rescale = 0.98


    # for bppattack
    parser.add_argument("--squeeze_num", type=int, default=32)
    parser.add_argument("--dithering", type=bool, default=False)

    # blended
    parser.add_argument("--blended_rate", type=int, default=0.2)
    parser.add_argument("--blended_trigger_path", type=str, default='data/triggers/hello_kitty.png')

    # issba
    parser.add_argument("--encorder_path", type=str, default=PREFIX+'data/ISSBA_encoder_ckpt')
    return parser
