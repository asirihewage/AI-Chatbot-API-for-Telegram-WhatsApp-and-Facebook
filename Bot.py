from allennlp.predictors.predictor import Predictor
import allennlp_models.rc

predictor = Predictor.from_path("model.tar.gz")
predictor.predict(
    passage="The Matrix is a 1999 science fiction action film written and directed by The Wachowskis, starring Keanu "
            "Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano.",
    question="Who stars in The Matrix?"
)