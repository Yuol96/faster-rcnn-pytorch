import torch
import torch.nn as nn

class FasterRCNN(nn.Module):
	def __init__(self, classes, class_agnostic):
		super(FasterRCNN, self).__init__()
		self.classes = classes
		self.class_agnostic = class_agnostic

		self.RCNN_base = self._build_RCNN_base()

		self.RCNN_rpn = 

	def _build_RCNN_base(self):
		raise NotImplementedError

	def forward(self, imgs, gtboxes):
		batch_size = imgs.size(0)

		gtboxes = gtboxes.data

		base_feat = self.RCNN_base(imgs)

