from django.db.models import Model


class Concept(Model):
    name = models.CharField(max_length=255)


class ConceptKeyword(Model):
    name = models.CharField(max_length=255)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name="keywords")


class ConceptStatus(Model):
    name = models.CharField(max_length=255)
    required_keywords = models.ManyToMany(ConceptKeyword)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name="statuses")


class Step(Model):
    name = models.CharField(max_length=255)
    desired_status = models.ForeignKey(ConceptStatus, on_delete=models.CASCADE, related_name="steps")
    step_at_fail = models.ForeignKey("self", on_delete=models.CASCADE, related_name="steps_from_failure")
    step_at_succeed = models.ForeignKey("self", on_delete=models.CASCADE, related_name="steps_from_success")
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name="steps")


class Dialog(Model):
    name = models.CharField(max_length=255)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, null=True, related_name="dialogs")
