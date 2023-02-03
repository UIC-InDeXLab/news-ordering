from scipy import stats


# run statistical test on user study results

with open("results_2023-02-02-6pm_sanitized.txt") as f:
	results = f.readlines()[3:]
	test = results[0]
	control = results[1]

	test_neg = int(test[10:12])
	test_pos = int(test[14:16])
	control_neg = int(control[10:12])
	control_pos = int(control[14:16])

	contingency_table = [[test_neg, control_neg], [test_pos, control_pos]]

	res = stats.boschloo_exact(contingency_table, alternative="greater", n=256)
	# res = stats.barnard_exact(contingency_table, alternative="greater", pooled=True, n=256)  # an alternative test that is also statistically valid but generally not as powerful

	pvalue = round(res.pvalue, 4)
	print(f"p={pvalue}")