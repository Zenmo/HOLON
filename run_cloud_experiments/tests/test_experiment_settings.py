from experiments.experiment_settings import ExperimentSettings

def test_setting():
    settings = ExperimentSettings.load()

    for setting in settings.all():
        assert 'show_progress' in setting
        assert 'name' in setting
        assert setting['timestep_hours'] > 0
