#from deeplightning.utils.metrics import metric_accuracy
from deeplightning.utils.metrics import Metric_Accuracy, Metric_ConfusionMatrix, Metric_PrecisionRecallCurve
from deeplightning.logger.wandb import wandbLogger
from deeplightning.trainer.hooks.ImageClassification_hooks import (
    training_step__ImageClassification,
    training_step_end__ImageClassification,
    training_epoch_end__ImageClassification,
    validation_step__ImageClassification,
    validation_step_end__ImageClassification,
    validation_epoch_end__ImageClassification,
    test_step__ImageClassification,
    test_step_end__ImageClassification,
    test_epoch_end__ImageClassification)
"""
from deeplightning.trainer.hooks.AudioClassification_hooks import (
    training_step__AudioClassification,
    training_step_end__AudioClassification,
    training_epoch_end__AudioClassification,
    validation_step__AudioClassification,
    validation_step_end__AudioClassification,
    validation_epoch_end__AudioClassification,
    test_step__AudioClassification,
    test_step_end__AudioClassification,
    test_epoch_end__AudioClassification)
"""


__TaskRegistry__ = [
    # Image
    "ImageClassification",
    "ImageReconstruction",
    "ObjectDetection",
    # Audio
    "AudioClassification",
]

__HooksRegistry__ = {
    # Image
    "ImageClassification": {
        "training_step": training_step__ImageClassification,
        "training_step_end": training_step_end__ImageClassification,
        "training_epoch_end": training_epoch_end__ImageClassification,
        "validation_step": validation_step__ImageClassification,
        "validation_step_end": validation_step_end__ImageClassification,
        "validation_epoch_end": validation_epoch_end__ImageClassification,
        "test_step": test_step__ImageClassification,
        "test_step_end": test_step_end__ImageClassification,
        "test_epoch_end": test_epoch_end__ImageClassification,
        "LOGGED_METRICS_NAMES": [
            "train_loss", "train_acc", 
            "val_loss", "val_acc", "val_confusion_matrix", "val_precision_recall",
            "test_loss", "test_acc", "test_confusion_matrix", "test_precision_recall",
            "lr"],
    },
    # Audio
    "AudioClassification": {
        "_": None,
    },
}


__MetricsRegistry__ = {
    # Image
	"ImageClassification": {
        "Accuracy_train": Metric_Accuracy,
        "Accuracy_val": Metric_Accuracy,
        "Accuracy_test": Metric_Accuracy,
        "ConfusionMatrix_val": Metric_ConfusionMatrix,
        "ConfusionMatrix_test": Metric_ConfusionMatrix,
		"PrecisionRecallCurve_val": Metric_PrecisionRecallCurve,
		"PrecisionRecallCurve_test": Metric_PrecisionRecallCurve,
	},
    "ImageReconstruction": {
        "_": None,
    },
    "ObjectDetection": {
        "_": None,
    },
    # Audio
    "AudioClassification":{
        "Accuracy": Metric_Accuracy,
        "ConfusionMatrix": Metric_ConfusionMatrix,
		"PrecisionRecallCurve": Metric_PrecisionRecallCurve,
    },
}


__LoggerRegistry__ = {
    "wandb": wandbLogger,
}
