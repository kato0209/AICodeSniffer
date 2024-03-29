package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"math"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

type NeuralNetwork struct {
	inputSize  int
	hiddenSize int
	outputSize int
	weights1   [][]float64
	weights2   [][]float64
	bias1      []float64
	bias2      []float64
}

func sigmoid(x float64) float64 {
	return 1.0 / (1.0 + math.Exp(-x))
}

func sigmoidDerivative(x float64) float64 {
	return sigmoid(x) * (1 - sigmoid(x))
}

func relu(x float64) float64 {
	if x >= 0 {
		return x
	} else {
		return 0
	}
}

func reluDerivative(x float64) float64 {
	if x >= 0 {
		return 1
	} else {
		return 0
	}
}

func NewNeuralNetwork(inputSize, hiddenSize, outputSize int) *NeuralNetwork {
	nn := &NeuralNetwork{
		inputSize:  inputSize,
		hiddenSize: hiddenSize,
		outputSize: outputSize,
		weights1:   make([][]float64, inputSize),
		weights2:   make([][]float64, hiddenSize),
		bias1:      make([]float64, hiddenSize),
		bias2:      make([]float64, outputSize),
	}

	rand.Seed(time.Now().UnixNano())

	for i := range nn.weights1 {
		nn.weights1[i] = make([]float64, nn.hiddenSize)
		for j := range nn.weights1[i] {
			nn.weights1[i][j] = rand.Float64()
		}
	}

	for i := range nn.weights2 {
		nn.weights2[i] = make([]float64, nn.outputSize)
		for j := range nn.weights2[i] {
			nn.weights2[i][j] = rand.Float64()
		}
	}

	for i := range nn.bias1 {
		nn.bias1[i] = rand.Float64()
	}

	for i := range nn.bias2 {
		nn.bias2[i] = rand.Float64()
	}

	return nn
}

func (nn *NeuralNetwork) Forward(input []float64) []float64 {
	hidden := make([]float64, nn.hiddenSize)
	output := make([]float64, nn.outputSize)

	for i := range hidden {
		for j := range input {
			hidden[i] += input[j] * nn.weights1[j][i]
		}
		hidden[i] = relu(hidden[i] + nn.bias1[i])
	}

	for i := range output {
		for j := range hidden {
			output[i] += hidden[j] * nn.weights2[j][i]
		}
		output[i] = sigmoid(output[i] + nn.bias2[i])
	}

	return output
}

func (nn *NeuralNetwork) TrainNeuralNetwork(inputs [][]float64, outputs [][]float64, learningRate float64, epochs int) {
	for epoch := 0; epoch < epochs; epoch++ {
		correct := 0 // 正解数をカウントするための変数
		for i := range inputs {
			input := inputs[i]
			output := outputs[i]
			hidden := make([]float64, nn.hiddenSize)
			outputLayer := make([]float64, nn.outputSize)

			// Forward propagation
			for j := range hidden {
				for k := range input {
					hidden[j] += input[k] * nn.weights1[k][j]
				}
				hidden[j] = relu(hidden[j] + nn.bias1[j])
			}

			for j := range outputLayer {
				for k := range hidden {
					outputLayer[j] += hidden[k] * nn.weights2[k][j]
				}
				outputLayer[j] = sigmoid(outputLayer[j] + nn.bias2[j])
			}

			// 正解数をカウントする
			prediction := 0
			for j, val := range outputLayer {
				if val > outputLayer[prediction] {
					prediction = j
				}
			}
			if output[prediction] == 1 {
				correct++
			}

			// Backpropagation
			outputLayerError := make([]float64, nn.outputSize)
			for j := range outputLayer {
				outputLayerError[j] = output[j] - outputLayer[j]
			}

			outputLayerDelta := make([]float64, nn.outputSize)
			for j := range outputLayerDelta {
				outputLayerDelta[j] = outputLayerError[j] * sigmoidDerivative(outputLayer[j])
			}

			hiddenError := make([]float64, nn.hiddenSize)
			for j := range hidden {
				for k := range outputLayerDelta {
					hiddenError[j] += outputLayerDelta[k] * nn.weights2[j][k]
				}
			}

			hiddenDelta := make([]float64, nn.hiddenSize)
			for j := range hiddenDelta {
				hiddenDelta[j] = hiddenError[j] * reluDerivative(hidden[j])
			}

			// Update weights and biases
			for j := range nn.bias2 {
				nn.bias2[j] += learningRate * outputLayerDelta[j]
				for k := range hidden {
					nn.weights2[k][j] += learningRate * outputLayerDelta[j] * hidden[k]
				}
			}

			for j := range nn.bias1 {
				nn.bias1[j] += learningRate * hiddenDelta[j]
				for k := range input {
					nn.weights1[k][j] += learningRate * hiddenDelta[j] * input[k]
				}
			}
		}

		// トレーニングセット全体に対する正答率を出力する
		accuracy := float64(correct) / float64(len(inputs)) * 100.0
		fmt.Printf("epoch: %d, accuracy: %f\n", epoch, accuracy)
	}
}

func ReadCSVFile(filename string) ([][]float64, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	reader := csv.NewReader(bufio.NewReader(file))
	var data [][]float64
	for {
		record, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			return nil, err
		}
		row := make([]float64, len(record))
		for i, v := range record {
			val, err := strconv.ParseFloat(strings.TrimSpace(v), 64)
			if err != nil {
				return nil, err
			}
			// row[i] = val
			if i != 0 {
				row[i] = val/256.0 + 0.0001
			} else {
				row[0] = val
			}
		}
		data = append(data, row)
	}
	return data, nil
}

func main() {
	// Load training data
	inputs, err := ReadCSVFile("data/mnist_train.csv")
	if err != nil {
		log.Fatal(err)
	}
	// Create one-hot encoded labels
	labels := [][]float64{
		{1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 1, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
	}

	// make outputs
	outputs := [][]float64{}
	for _, input := range inputs {
		outputs = append(outputs, labels[int(input[0])])
	}

	// Train neural network
	nn := NewNeuralNetwork(len(inputs[0]), 64, len(labels[0]))
	nn.TrainNeuralNetwork(inputs, outputs, 0.01, 50)

	// Load test data
	testInputs, err := ReadCSVFile("data/mnist_test.csv")
	if err != nil {
		log.Fatal(err)
	}

	// Test neural network
	ca := 0
	for i := range testInputs {
		outputs := nn.Forward(testInputs[i])
		bestIndex := 0
		bestValue := 0.0

		for j := range outputs {
			if outputs[j] > bestValue {
				bestValue = outputs[j]
				bestIndex = j
			}
		}
		fmt.Printf("Predicted: %d ,Correct answer: %d \n", bestIndex, int(testInputs[i][0]))
		if bestIndex == int(testInputs[i][0]) {
			ca++
		}
	}
	fmt.Printf("Correct answer rate: %d / %d", ca, len(testInputs))
}
