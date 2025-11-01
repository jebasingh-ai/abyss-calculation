#!/usr/bin/env python3
"""
🏎️ Abyss Calculation Performance Benchmark
The Most Comprehensive 1+1 Performance Test in the Multiverse
"""

import time
import subprocess
import json
import statistics
from datetime import datetime
import sys

class AbyssBenchmark:
    def __init__(self):
        self.results = {}
        self.languages = {
            'python': {
                'command': 'cd src/python && python3 -c "from abyss import quick_calculation; quick_calculation()"',
                'type': 'normal'
            },
            'python_drama': {
                'command': 'cd src/python && python3 -c "from abyss import descend; descend()"',
                'type': 'dramatic'
            },
            'javascript': {
                'command': 'cd src/javascript && node -e "require(\"./abyss.js\").abyssCalculation().then(console.log)"',
                'type': 'normal'
            },
            'typescript': {
                'command': 'cd src/typescript && npx ts-node -e "import AbyssCalculation from \"./abyss\"; AbyssCalculation.quickCalculation().then(console.log)"',
                'type': 'normal'
            },
            'rust': {
                'command': 'cd src/rust && ./target/release/abyss_calculation',
                'type': 'normal'
            },
            'go': {
                'command': 'cd src/go && ./abyss',
                'type': 'normal'
            },
            'java': {
                'command': 'cd src/java && java AbyssCalculator',
                'type': 'normal'
            },
            'cpp': {
                'command': 'cd src/cpp && ./abyss_cpp',
                'type': 'normal'
            },
            'brainfuck': {
                'command': 'cd src/brainfuck && brainfuck abyss.bf',
                'type': 'esoteric'
            },
            'lolcode': {
                'command': 'cd src/Lolcode && lci abyss.lol',
                'type': 'esoteric'
            },
            'ruby': {
                'command': 'cd src/ruby && ruby abyss.rb',
                'type': 'normal'
            },
            'php': {
                'command': 'cd src/php && php abyss.php',
                'type': 'normal'
            },
            # Add more languages as needed...
        }
    
    def run_benchmark(self, language, command, runs=3):
        """Run benchmark for a single language"""
        print(f"⏱️  Benchmarking {language:12}...", end=" ")
        sys.stdout.flush()
        
        times = []
        for i in range(runs):
            start_time = time.time()
            try:
                result = subprocess.run(
                    command, 
                    shell=True, 
                    capture_output=True, 
                    text=True,
                    timeout=30  # 30 second timeout
                )
                if result.returncode == 0:
                    elapsed = time.time() - start_time
                    times.append(elapsed)
                else:
                    print(f"❌ (Run {i+1} failed)")
                    return None
            except subprocess.TimeoutExpired:
                print(f"⏰ (Run {i+1} timed out)")
                return None
            except Exception as e:
                print(f"💥 (Run {i+1} error: {e})")
                return None
        
        if times:
            avg_time = statistics.mean(times)
            std_dev = statistics.stdev(times) if len(times) > 1 else 0
            print(f"✅ {avg_time:.4f}s ± {std_dev:.4f}s")
            return {
                'language': language,
                'type': self.languages[language]['type'],
                'average_time': avg_time,
                'std_dev': std_dev,
                'runs': runs,
                'times': times
            }
        else:
            print("❌ No successful runs")
            return None
    
    def run_all_benchmarks(self):
        """Run benchmarks for all languages"""
        print("🏎️" + "="*60)
        print("   ABYSS CALCULATION PERFORMANCE BENCHMARK")
        print("   The Most Comprehensive 1+1 Speed Test")
        print("="*60)
        print()
        
        successful_benchmarks = 0
        
        for lang, info in self.languages.items():
            result = self.run_benchmark(lang, info['command'])
            if result:
                self.results[lang] = result
                successful_benchmarks += 1
        
        return successful_benchmarks
    
    def generate_report(self):
        """Generate comprehensive benchmark report"""
        if not self.results:
            print("❌ No successful benchmarks to report")
            return
        
        # Sort by average time
        sorted_results = sorted(
            self.results.values(), 
            key=lambda x: x['average_time']
        )
        
        print("\n📊" + "="*60)
        print("   BENCHMARK RESULTS SUMMARY")
        print("="*60)
        
        print(f"\n🏆 PERFORMANCE RANKINGS:")
        print("-" * 50)
        for i, result in enumerate(sorted_results, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i:2d}"
            print(f"{medal} {result['language']:15} : {result['average_time']:.6f}s ± {result['std_dev']:.6f}s")
        
        # Statistics by type
        normal_times = [r['average_time'] for r in self.results.values() if r['type'] == 'normal']
        esoteric_times = [r['average_time'] for r in self.results.values() if r['type'] == 'esoteric']
        dramatic_times = [r['average_time'] for r in self.results.values() if r['type'] == 'dramatic']
        
        print(f"\n📈 STATISTICS BY CATEGORY:")
        print("-" * 50)
        if normal_times:
            print(f"🔧 Normal languages    : {statistics.mean(normal_times):.6f}s (n={len(normal_times)})")
        if esoteric_times:
            print(f"🤪 Esoteric languages  : {statistics.mean(esoteric_times):.6f}s (n={len(esoteric_times)})")
        if dramatic_times:
            print(f"🎭 Dramatic versions   : {statistics.mean(dramatic_times):.6f}s (n={len(dramatic_times)})")
        
        # Save results to JSON
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_languages_tested': len(self.results),
            'results': self.results,
            'summary': {
                'fastest': sorted_results[0]['language'],
                'slowest': sorted_results[-1]['language'],
                'fastest_time': sorted_results[0]['average_time'],
                'slowest_time': sorted_results[-1]['average_time']
            }
        }
        
        with open('benchmark_results.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 Full results saved to: benchmark_results.json")
        
        # Final wisdom
        print(f"\n🎯 FINAL WISDOM:")
        print("-" * 50)
        fastest = sorted_results[0]
        slowest = sorted_results[-1]
        print(f"⚡ Fastest: {fastest['language']} ({fastest['average_time']:.6f}s)")
        print(f"🐌 Slowest: {slowest['language']} ({slowest['average_time']:.6f}s)")
        print(f"📏 Speed ratio: {slowest['average_time']/fastest['average_time']:.1f}x")
        print(f"💡 Conclusion: They all calculate 1+1=2. Choose wisely.")

def main():
    benchmark = AbyssBenchmark()
    
    successful = benchmark.run_all_benchmarks()
    
    if successful > 0:
        benchmark.generate_report()
        
        # Exit with success code
        sys.exit(0)
    else:
        print("❌ No benchmarks completed successfully")
        sys.exit(1)

if __name__ == "__main__":
    main()
