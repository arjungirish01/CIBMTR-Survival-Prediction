from sklearn.metrics import accuracy_score, roc_auc_score, log_loss
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter, CoxPHFitter

def evaluate_classifier(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    loss = log_loss(y_test, y_prob)

    return {"accuracy": acc, "roc_auc": auc, "log_loss": loss}

def plot_feature_importance(model, feature_names):
    if hasattr(model, "feature_importances_"):
        importance = model.feature_importances_
        sns.barplot(x=importance, y=feature_names)
        plt.title("Feature Importance")
        plt.show()

def survival_analysis(df, time_col, event_col):
    kmf = KaplanMeierFitter()
    kmf.fit(df[time_col], event_observed=df[event_col])
    kmf.plot_survival_function()
    plt.title("Kaplan-Meier Survival Curve")
    plt.show()

def cox_analysis(df, time_col, event_col):
    cph = CoxPHFitter()
    cph.fit(df, duration_col=time_col, event_col=event_col)
    cph.print_summary()
