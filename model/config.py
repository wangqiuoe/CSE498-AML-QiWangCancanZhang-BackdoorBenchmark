import argparse


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_root", type=str, default="./data")
    parser.add_argument("--checkpoints", type=str, default="./checkpoints/badnet")
    parser.add_argument("--temps", type=str, default="./temps")
    parser.add_argument("--device", type=str, default="cuda:1")
    parser.add_argument("--continue_training", action="store_true")

    parser.add_argument("--dataset", type=str, default="cifar10")
    parser.add_argument("--attack", type=str, default="BadNet")
    parser.add_argument("--attack_mode", type=str, default="all2one")

    parser.add_argument("--bs", type=int, default=128)
    parser.add_argument("--lr_C", type=float, default=1e-2)
    parser.add_argument("--schedulerC_milestones", type=list, default=[100, 200, 300, 400])
    parser.add_argument("--schedulerC_lambda", type=float, default=0.1)
    parser.add_argument("--n_iters", type=int, default=1000)
    parser.add_argument("--num_workers", type=float, default=6)

    parser.add_argument("--target_label", type=int, default=0)
    parser.add_argument("--pc", type=float, default=0.1)
    parser.add_argument("--cross_ratio", type=float, default=2)  # rho_a = pc, rho_n = pc * cross_ratio

    parser.add_argument("--random_rotation", type=int, default=10)
    parser.add_argument("--random_crop", type=int, default=5)

    parser.add_argument("--s", type=float, default=0.5)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument(
        "--grid-rescale", type=float, default=1
    )  # scale grid values to avoid pixel values going out of [-1, 1]. For example, grid-rescale = 0.98

    # bppattack
    parser.add_argument("--squeeze_num", type=int, default=8)
    parser.add_argument("--dithering", type=bool, default=False)
    parser.add_argument("--injection_rate", type=float, default=0.2)
    parser.add_argument("--neg_rate", type=float, default=0.2)
    parser.add_argument("--save_all", type=bool, default=False)
    parser.add_argument("--save_freq", type=int, default=50)
    parser.add_argument("--set_arch", type=str, default=None)

    # blended
    parser.add_argument("--blended_rate", type=int, default=0.2)
    parser.add_argument("--blended_trigger_path", type=str, default='data/triggers/hello_kitty.png')

    # issba
    parser.add_argument("--encorder_path", type=str, default='data/ISSBA_encoder_ckpt/')

    return parser
