# Deployment and Testing Strategy

## Overview
This document outlines the automated testing and deployment process for the ETL pipeline project.

## Testing Levels

### 1. Local Testing (Pre-Push)
**Trigger**: Before any git push
**Enforcer**: `.git/hooks/pre-push`

Tests run locally before push:
- ✅ All unit tests (pytest)
- ✅ Code coverage check (minimum 60%)
- ✅ Git status validation
- ✅ Branch synchronization check

**Command to run tests locally:**
```bash
pytest --cov=. --cov-fail-under=60 -v
```

### 2. CI/CD Pipeline Testing (GitHub Actions)
**Trigger**: On push to main or cicd_deployment_test branches
**Location**: `.github/workflows/test_and_deploy.yml`

Tests run automatically on GitHub:
- ✅ Install all dependencies
- ✅ Run pytest with coverage check (minimum 60%)
- ✅ Generate coverage reports (XML and HTML)
- ✅ Upload coverage to CodeCov
- ✅ Archive test results as artifacts

### 3. Deployment Gate
**Requirement**: All tests must pass
**Branch Protection**: Only deploy to main after all tests pass

## Deployment Pipeline

### For cicd_deployment_test Branch:
1. Developer makes changes
2. Local tests run (pre-push hook)
3. Push to cicd_deployment_test
4. GitHub Actions runs full test suite
5. Tests must pass for branch to be current

### For main Branch (Production):
1. Developer makes changes and tests locally
2. Push to feature branch (if applicable)
3. Create pull request to main
4. GitHub Actions runs full test suite on PR
5. Tests must pass before merge approval
6. Merge to main
7. GitHub Actions runs deployment pipeline
8. Production deployment only if all tests pass

## Test Requirements

### Coverage Threshold: 60%
All code must have at least 60% test coverage:
```
- data_loader.py: 71%
- transformer.py: 73%
- sales_merger.py: 55%
- snowflake_loader.py: 52%
- test_upload_script.py: 98%
- upload_script.py: 97%
- TOTAL: 64%
```

### Test Count: 10 Tests
All tests must pass:
1. test_data_loader_creates_files
2. test_transformer_merges_files
3. test_reader_reads_merged_file
4. test_upload_script_main
5. test_sales_merger_merges_files
6. test_snowflake_loader_validates_data
7. test_import_upload_script
8. test_dummy
9. test_upload_script_exists
10. test_excel_file_created

## Local Development Workflow

### 1. Setup Environment
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Make Changes
Edit your code and create/update tests

### 3. Run Local Tests
```bash
pytest --cov=. --cov-fail-under=60 -v
```

### 4. Commit Changes
```bash
git add .
git commit -m "Your commit message"
```

### 5. Pre-Push Validation
```bash
# Pre-push hook runs automatically
git push
# If tests fail, push is aborted
```

### 6. GitHub Actions Verification
- Go to Actions tab on GitHub
- Verify all tests pass
- Check coverage reports

## Deployment Checklist

Before deploying to production:
- [ ] All 10 tests passing locally
- [ ] Code coverage ≥ 60%
- [ ] GitHub Actions workflow passing
- [ ] No uncommitted changes
- [ ] Branch synchronized with remote
- [ ] PR approved (if applicable)
- [ ] Snowflake credentials configured
- [ ] SharePoint credentials configured (if needed)

## Rollback Procedure

If deployment fails in production:

1. Identify the failing commit
2. Revert to previous stable commit:
   ```bash
   git revert <commit-hash>
   ```
3. Push revert commit (tests must pass)
4. GitHub Actions will detect revert and fail deployment if needed
5. Investigate root cause
6. Fix issues and test locally
7. Create new commit with fixes
8. Re-deploy through normal pipeline

## Monitoring

### Local Monitoring
```bash
# Watch for test failures
pytest --cov=. --cov-fail-under=60 --tb=short

# View coverage report
start htmlcov/index.html
```

### GitHub Actions Monitoring
- Watch the Actions tab on GitHub
- Review test results and logs
- Download coverage artifacts
- Check CodeCov integration

## Troubleshooting

### Tests Failing Locally
1. Ensure all dependencies installed: `pip install -r requirements.txt`
2. Check Python version: `python --version` (requires 3.12+)
3. Clear cache: `rm -r __pycache__ .pytest_cache`
4. Run single test: `pytest tests/test_name.py -v`

### Pre-Push Hook Issues
1. Make hook executable: `chmod +x .git/hooks/pre-push`
2. Check venv path in hook
3. Try running tests manually: `.venv\Scripts\pytest`

### GitHub Actions Failure
1. Check workflow logs in Actions tab
2. Verify secrets/credentials configured
3. Check branch protection rules
4. Verify Python version compatibility

## Continuous Improvement

- Monitor test execution times
- Improve test coverage (target: 80%+)
- Add performance benchmarks
- Regular security scanning
- Update dependencies monthly

## Contact & Support

For deployment issues:
1. Check GitHub Actions logs
2. Review code changes
3. Run local tests with verbose output
4. Check pre-push hook configuration
5. Escalate if needed
