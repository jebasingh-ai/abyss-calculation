// 🐹 Abyss Calculation - Go Edition
// The Most Concurrent 1+1 Calculator with Goroutines!

package main

import (
    "fmt"
    "time"
    "sync"
    "context"
)

func quantumEntanglement(ctx context.Context, value int) <-chan int {
    ch := make(chan int)
    go func() {
        defer close(ch)
        fmt.Println("   🔮 Entangling quantum state...")
        select {
        case <-time.After(800 * time.Millisecond):
            ch <- value
        case <-ctx.Done():
            return
        }
    }()
    return ch
}

func main() {
    ctx := context.Background()
    
    var wg sync.WaitGroup
    results := make(chan int, 2)
    
    wg.Add(2)
    go func() {
        defer wg.Done()
        results <- <-quantumEntanglement(ctx, 1)
    }()
    go func() {
        defer wg.Done() 
        results <- <-quantumEntanglement(ctx, 1)
    }()
    
    go func() {
        wg.Wait()
        close(results)
    }()
    
    sum := 0
    for result := range results {
        sum += result
    }
    
    fmt.Printf("🎉 Result: %d (with goroutines!)\n", sum)
}
