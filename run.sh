#!/bin/bash
# Interactive setup menu for PyTorch PCD Metrics

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get project root directory
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Activate conda environment
if [ -z "$CONDA_DEFAULT_ENV" ] || [ "$CONDA_DEFAULT_ENV" != "gen3d" ]; then
    print_info() { echo -e "${YELLOW}ℹ $1${NC}"; }
    print_info "Activating conda environment 'gen3d'..."
    eval "$(conda shell.bash hook 2>/dev/null)" || true
    conda activate gen3d 2>/dev/null || {
        echo -e "${RED}✗ Failed to activate conda environment 'gen3d'${NC}"
        echo -e "${YELLOW}ℹ Please run: conda activate gen3d${NC}"
        echo -e "${YELLOW}ℹ Then run this script again${NC}"
        exit 1
    }
fi

# Function to print colored messages
print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

# Function to install/update conda environment
install_conda_env() {
    print_header "Installing/Updating Conda Environment 'gen3d'"

    if [ ! -f "$PROJECT_ROOT/environment.yml" ]; then
        print_error "environment.yml not found!"
        return 1
    fi

    print_info "Checking if conda is available..."
    if ! command -v conda &> /dev/null; then
        print_error "conda not found! Please install Miniconda or Anaconda first."
        return 1
    fi

    print_info "Creating/Updating environment from environment.yml..."
    conda env update -f "$PROJECT_ROOT/environment.yml" --prune

    print_success "Environment 'gen3d' is ready!"
    print_info "Activate with: conda activate gen3d"
    echo ""
}

# Function to ensure conda environment is activated
ensure_conda_env() {
    if [ -z "$CONDA_DEFAULT_ENV" ] || [ "$CONDA_DEFAULT_ENV" != "gen3d" ]; then
        print_info "Activating conda environment 'gen3d'..."
        eval "$(conda shell.bash hook)"
        conda activate gen3d
        if [ $? -ne 0 ]; then
            print_error "Failed to activate conda environment 'gen3d'"
            print_info "Please run: conda activate gen3d"
            return 1
        fi
        print_success "Conda environment 'gen3d' activated"
        echo ""
    else
        print_info "Already in conda environment: $CONDA_DEFAULT_ENV"
        echo ""
    fi
}

# Function to install PCD metric packages
install_pcd_packages() {
    print_header "Installing PCD Metric Packages"

    ensure_conda_env || return 1

    print_info "Installing PointFlow StructuralLosses..."
    cd "$PROJECT_ROOT/sources/modified/PointFlow__pytorch_structural_losses"
    pip install --no-build-isolation .
    print_success "PointFlow StructuralLosses installed"
    echo ""

    print_info "Installing MSN EMD..."
    cd "$PROJECT_ROOT/sources/modified/MSN__emd"
    pip install --no-build-isolation .
    print_success "MSN EMD installed"
    echo ""

    print_info "Installing PyTorchEMD..."
    cd "$PROJECT_ROOT/sources/modified/daerduoCarey__PyTorchEMD"
    pip install --no-build-isolation .
    print_success "PyTorchEMD installed"
    echo ""

    print_info "Installing ChamferDistance..."
    cd "$PROJECT_ROOT/sources/modified/ThibaultGROUEIX__ChamferDistancePytorch/chamfer3D"
    pip install --no-build-isolation .
    print_success "ChamferDistance installed"
    echo ""

    cd "$PROJECT_ROOT"
    print_success "All PCD metric packages installed successfully!"
    echo ""
}

# Function to install unified wrapper
install_wrapper() {
    print_header "Installing Unified Wrapper Package"

    ensure_conda_env || return 1

    cd "$PROJECT_ROOT"
    print_info "Installing pytorch_pcd_metrics wrapper..."
    pip install .

    print_success "Unified wrapper installed!"
    print_info "You can now use: from pytorch_pcd_metrics.emd import emdModule"
    echo ""
}

# Function to run tests
run_tests() {
    print_header "Running Tests"

    if [ ! -f "$PROJECT_ROOT/notebooks/test_evaluation_metrics.ipynb" ]; then
        print_error "Test notebook not found!"
        return 1
    fi

    print_info "Opening test notebook..."
    cd "$PROJECT_ROOT/notebooks"

    if command -v jupyter &> /dev/null; then
        jupyter notebook test_evaluation_metrics.ipynb
    else
        print_error "Jupyter not found! Install with: pip install jupyter"
        print_info "Or activate the 'gen3d' environment: conda activate gen3d"
        return 1
    fi
}

# Function to run tests
run_tests() {
    print_header "Running Tests"

    ensure_conda_env || return 1

    cd "$PROJECT_ROOT"
    print_info "Converting notebook to Python script..."
    jupyter nbconvert --to python "notebooks/01_test_packages.ipynb" --output "01_test_packages" >/dev/null 2>&1

    print_info "Running tests..."
    python notebooks/01_test_packages.py

    print_info "Cleaning up..."
    rm -f notebooks/01_test_packages.py

    echo ""
}

# Function to clean build artifacts
clean_artifacts() {
    print_header "Cleaning Build Artifacts"

    cd "$PROJECT_ROOT"
    print_info "Removing build artifacts..."

    find . -type d \( -name "build" -o -name "*.egg-info" -o -name "__pycache__" -o -name "dist" \) -exec rm -rf {} + 2>/dev/null || true
    find . -type f \( -name "*.pyc" -o -name "*.pyo" -o -name "*.so" \) -delete 2>/dev/null || true

    print_success "Build artifacts cleaned!"
    echo ""
}

# Function to display menu
show_menu() {
    echo ""
    print_header "PyTorch PCD Metrics - Setup Menu"
    echo "1. Install/Update conda environment 'gen3d'"
    echo "2. Install PCD metric packages (PointFlow + MSN EMD + PyTorchEMD + ChamferDistance)"
    echo "3. Install unified wrapper package"
    echo "4. Install everything (1 + 2 + 3)"
    echo "5. Clean build artifacts"
    echo "6. Run tests"
    echo "0. Exit"
    echo ""
}

# Main menu loop
main() {
    while true; do
        show_menu
        read -p "Choose an option [0-6]: " choice
        echo ""

        case $choice in
            0|"")
                print_info "Exiting..."
                exit 0
                ;;
            1)
                install_conda_env
                ;;
            2)
                install_pcd_packages
                ;;
            3)
                install_wrapper
                ;;
            4)
                install_conda_env
                install_pcd_packages
                install_wrapper
                print_success "Complete installation finished!"
                echo ""
                ;;
            5)
                clean_artifacts
                ;;
            6)
                run_tests
                ;;
            *)
                print_error "Invalid option. Please choose 0-6."
                ;;
        esac

        if [ "$choice" != "0" ] && [ -n "$choice" ]; then
            read -p "Press Enter to continue..."
        fi
    done
}

# Check for command-line argument
if [ $# -eq 1 ]; then
    choice=$1
    case $choice in
        1)
            install_conda_env
            ;;
        2)
            install_pcd_packages
            ;;
        3)
            install_wrapper
            ;;
        4)
            install_conda_env
            install_pcd_packages
            install_wrapper
            print_success "Complete installation finished!"
            echo ""
            ;;
        5)
            clean_artifacts
            ;;
        6)
            run_tests
            ;;
        *)
            print_error "Invalid option. Please choose 1-6."
            exit 1
            ;;
    esac
else
    # Run interactive menu
    main
fi
