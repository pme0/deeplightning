import argparse

import hydra
from omegaconf import DictConfig
import wandb

from deeplightning.config.dlconfig import DeepLightningConfig
from deeplightning.core.dlpipeline import DeepLightningPipeline
from deeplightning.utils.context import train_context, eval_context


parser = argparse.ArgumentParser()
parser.add_argument(
    "--config-name", 
    type=str, 
    help="Filename of YAML configuration file. Overwrites `config_name` in hydra.main()."
)
parser.add_argument(
    "--config-path", 
    type=str, 
    default="configs", 
    help="Directory of YAML configuration file. Overwrites `config_path` in hydra.main()."
)
args = parser.parse_args()


@hydra.main(
    version_base=None,
    config_path=args.config_path, 
    config_name=args.config_name,
)
def _main(config: DictConfig) -> None:
    """Main function running initializations, training and evaluation."""
    
    # The following config is incomplete. When initializing the trainer within
    # the Pipeline, the config will be updated with runtime info (e.g. run id,
    # created by the logger). Below we will retrieve the complete config.
    cfg = DeepLightningConfig(config)
    cfg.print_config()

    # Instantiate pipeline.
    pipeline = DeepLightningPipeline(cfg)

    # Retrieve config updated with runtime info.
    cfg = pipeline.cfg
    cfg.print_config()
    cfg.log_config()
    

    with train_context(cfg.engine.seed):
        if cfg.stages.train.active:
            pipeline.train()
  
    with eval_context(cfg.engine.seed):
        if cfg.stages.train.active:
            pipeline.eval("best")
        elif cfg.stages.test.active:
            pipeline.eval("config")

    wandb.finish()


if __name__ == "__main__":
    _main()