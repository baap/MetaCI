# Generated by Django 2.2.5 on 2019-10-03 14:15

from django.db import migrations


def set_plan_queues(apps, schema_editor):
    Plan = apps.get_model("plan", "Plan")
    # Use medium queue for plans triggered manually or by tags
    Plan.objects.filter(trigger__in=("manual", "tag")).update(queue="medium")
    # Use high queue for plans that use a packaging org
    Plan.objects.filter(org="packaging").update(queue="high")


class Migration(migrations.Migration):

    dependencies = [("plan", "0031_plan_queue")]

    operations = [migrations.RunPython(set_plan_queues)]
